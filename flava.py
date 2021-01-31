import os
import requests
import json
os.environ["EAI_USERNAME"] = 'YOUR EAI USERNAME'
os.environ["EAI_PASSWORD"] = 'YOUR EAI PASSWORD'

from expertai.nlapi.cloud.client import ExpertAiClient
client = ExpertAiClient()

# GET RESTAURANT
searchTerm = input("Enter a business name or search term: ")
searchLocation = input("Enter a city name or zip code: ")

MY_API_KEY = "YELP API KEY GOES HERE"
googleAPIKey = "GOOGLE API KEY GOES HERE"
language= 'en'

masterText = ""
masterList  = []

# Search for business on Yelp first
url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': f"Bearer {MY_API_KEY}"}
params={'term':searchTerm, 'location':searchLocation}

resp = requests.get(url, params=params, headers=headers)
parsed = json.loads(resp.text)

thebusinesses = parsed["businesses"]

# Get precise business name and Yelp ID
myBizName = thebusinesses[0]["name"]
myBizID = thebusinesses[0]["id"]

# Get the Yelp reviewss
url = 'https://api.yelp.com/v3/businesses/' + myBizID + '/reviews'
resp = requests.get(url, headers=headers)
parsed = json.loads(resp.text)

thereviews = parsed["reviews"]

for theYelpReview in thereviews:
    #print (theYelpReview["text"])
    document = client.specific_resource_analysis(
        body={"document": {"text": theYelpReview["text"]}},
        params={'language': language, 'resource': 'sentiment'})

    # Add sentiment scores to our masterList
    masterList.append(document.sentiment.overall)


# Get Google Places info
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query=' + myBizName + '+' + searchLocation + '&key=' + googleAPIKey
resp = requests.get(url)
parsed = json.loads(resp.text)
googleSearch = parsed["results"]

googleBizName = googleSearch[0]["name"]
googleBizID = googleSearch[0]["place_id"]

# Get Google Maps reviews, and add the sentiment score for each to our masterList
url = 'https://maps.googleapis.com/maps/api/place/details/json?place_id=' + googleBizID + '&fields=name,rating,reviews,formatted_address&key=' + googleAPIKey
resp = requests.get(url)
parsed = json.loads(resp.text)
googleReviews = parsed["result"]["reviews"]
formattedAddress = parsed["result"]["formatted_address"]

for theGoogleReview in googleReviews:
    #print (theGoogleReview["text"])
    document = client.specific_resource_analysis(
        body={"document": {"text": theGoogleReview["text"]}},
        params={'language': language, 'resource': 'sentiment'})

    masterList.append(document.sentiment.overall)


# The final FLAVA rating is then put into 4 ranges: "Hated", "Meh", "Liked", or "Loved"

theFinalScore = round(sum(masterList) / len(masterList),2)
print ("Final score: " + str(theFinalScore))

if theFinalScore > 2 and theFinalScore < 10:
    print ("LIKED - you'll dig it.")

if theFinalScore > 10:
    print ("LOVED - you'll love this place.")

if theFinalScore < 2 and theFinalScore > -6:
    print ("MEH - it's alright.")

if theFinalScore < -6:
    print ("HATED - definitely not a favorite.")
