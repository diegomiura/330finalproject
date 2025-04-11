# tweeting.py

import tweepy
from credentials import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def create_twitter_client():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def post_tweet(text):
    api = create_twitter_client()
    try:
        api.update_status(text)
        print("Tweeted successfully!")
    except Exception as e:
        print("Error while tweeting:", e)

if __name__ == "__main__":
    post_tweet("Hello world! 🚀 This is my first automated tweet.")