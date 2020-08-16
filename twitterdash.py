from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time

analyzer = SentimentIntensityAnalyzer()

conn = sqlite3.connect('twitter2.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, neg_sentiment REAL,neu_sentiment REAL,pos_sentiment REAL,com_sentiment REAL)")
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_neg_sentiment ON sentiment(neg_sentiment)")
        c.execute("CREATE INDEX fast_neu_sentiment ON sentiment(neu_sentiment)")
        c.execute("CREATE INDEX fast_pos_sentiment ON sentiment(pos_sentiment)")
        c.execute("CREATE INDEX fast_com_sentiment ON sentiment(com_sentiment)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()



#consumer key, consumer secret, access token, access secret.
ckey='iym0XRG0SOgyPOjmlPQgB4XrC'
csecret='I6gBj8RpcXJvN6xaKUUGeTkPEDpHziRXBmT9d9yG8k5Ik0H0bF'
atoken='727494459118653446-XWf9MmBJmCUOM7Ic9xvoHlZCBQAWWA1'
asecret='jl4UJPXYSC8ygV8EsyNz6fMOW2NEs9NFvJc2InyfXNvve'



class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = unidecode(data['text'])
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            neg_sentiment = vs['neg']
            neu_sentiment = vs['neu']
            pos_sentiment = vs['pos']
            com_sentiment = vs['compound']
            print(vs)
            print(time_ms, tweet, pos_sentiment)
            c.execute("INSERT INTO sentiment (unix, tweet, neg_sentiment,neu_sentiment,pos_sentiment,com_sentiment) VALUES (?, ?, ?,?,?,?)",
                  (time_ms, tweet, neg_sentiment,neu_sentiment,pos_sentiment,com_sentiment))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)
    

while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["biden"])
    except Exception as e:
        print(str(e))
        time.sleep(12)