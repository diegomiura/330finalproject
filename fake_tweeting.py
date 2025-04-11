import tweepy
from credentials import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from fact_generator import get_fact

def create_twitter_client():
    pass  # This function is no longer used

def post_tweet(text):
    print(f"[SIMULATED TWEET] {text}")

if __name__ == "__main__":
    fact = get_fact()
    post_tweet(fact)