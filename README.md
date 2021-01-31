# FLAVA
Local business reviews powered by natural language sentiment AI. Find out whether you will love or hate a restaurant, hotel, or apartment with greater accuracy.

## How to use

This repo contains a single Python script that can be run from the terminal. In the demo/production version of FLAVA, I built an HTML user-friendly interface. Try that out here: https://contrabandinteractive.com/flava/

If you'd like to run this script, you will need to have the following:
Yelp API Key, Google API Key with Places enabled, and an expert.ai Natural Language API account.

Add your credentials to these lines: 4, 5, 14, and 15.

## Inspiration

FLAVA is based on the theory that the words people use when describing their experiences often reveal a more accurate depiction of true thoughts and feelings compared to a number rating.  Many review sites offer reviewers a chance to assign a 1 to 5 rating to a local business, often accompanied with a text description with more details of their experience.

Simple number ratings can often be unreliable due to several factors: they don't capture the true sentiment of the reviewer. However, if we can determine a rating based on text alone (taking the ability to choose an arbitrary number rating away from reviewers), we suspect that we will get a more accurate review overall. 

## What it does

FLAVA pulls in reviews from leading sites such as Yelp and Google Maps. Review text is then run through the expert.ai Natural Language API to determine the sentiment. The average sentiment value of the reviews is then used to give the final FLAVA rating, which will categorize local businesses within one of the four: LOVED, LIKED, MEH, or HATED.

## Hackathon

This is an official submission for to the expert.ai Hackathon on Devpost.
