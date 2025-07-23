import os
from dotenv import load_dotenv
import tweepy
import requests

load_dotenv()


def scrape_user_tweets(username, mock=False):
    tweet_list = []

    if mock:
        EDEN_TWITTER_GIST = "https://gist.githubusercontent.com/emarco177/827323bb599553d0f0e662da07b9ff68/raw/57bf38cf8acce0c87e060f9bb51f6ab72098fbd6/eden-marco-twitter.json"

        tweets = requests.get(EDEN_TWITTER_GIST).json()
        
        for tweet in tweets:
            tweet_dict = {}
            tweet_dict["text"] = tweet["text"]
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
            tweet_list.append(tweet_dict)
    
    return tweet_list

if __name__ == "__main__":
    print(scrape_user_tweets("EdenEmarco177", mock=True))

