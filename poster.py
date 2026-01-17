import tweepy
import os
import json
from dotenv import load_dotenv

class XPoster:
    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(
            bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        )
        
    def post(self, text, thread_id=None):
        try:
            if thread_id:
                response = self.client.create_tweet(
                    text=text, 
                    quote_tweet_id=thread_id
                )
            else:
                response = self.client.create_tweet(text=text)

            return response.data['id']
        except Exception as e:
            print(f"Error posting to X: {e}")
            return None