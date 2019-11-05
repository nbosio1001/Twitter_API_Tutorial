from tweepy.streaming import StreamListener # Allows to listen to tweets as they appear based on keywords
from tweepy import OAuthHandler # Responsible for authentics based on credentials written in twitter_credentials file
from tweepy import Stream

import twitter_credentials

class StdOutListener(StreamListener): # Allows to print tweets, inherits from StreamListener class
    def on_data(self, data): # Take the data that listens for Tweets
        print(data)
        return True
    def on_error(self, status): # Method overriding from StreamListener class if error occurs
        print(status)

if __name__ == "__main__":
    listener=StdOutListner()
    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET) # Authenticates code
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = Stream(auth, listner)
    
    stream.filter(track=['Tesla','tesla','Elon','Elon Musk']) # Listen of things if tweet contains any list objects, will add to the stream
