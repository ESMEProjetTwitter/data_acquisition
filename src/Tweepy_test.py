import tweepy
from tweepy import OAuthHandler
import json
import pandas as pd 
import matplotlib.pyplot as plt


client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAACNWaQEAAAAAQaaBxfOjJCX1m3H%2BF0qrSGFIKPc%3DQxdEvIXQi90IT32aQ8JDcOmxgnp34idYC5H712BzQfybgyRv9r')


with open("twitter_credentials.auth.json", 'r') as file :
    credentials = json.load(file)

authentification_handler = OAuthHandler (
    consumer_key= credentials['api-key'],
    consumer_secret= credentials ['api-key-secret']
) 

authentification_handler.set_access_token (
    key = credentials ['access-token'],
    secret = credentials ['access-token-secret']
)


query = '#macron  -is:retweet'

response = client.search_recent_tweets(query=query, tweet_fields=['created_at','lang'], user_fields = ['location'], max_results=10)


for tweet in response.data:
    print(type(tweet))
    print(tweet["created_at"])
    print(tweet["geo"])
    print(tweet["lang"])    
 
 

    


"""

query = 'pomme -is:retweet'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)


df = pd.DataFrame(counts.data)
Jour =  ['-7','-6','-5','-4','-3','-2','-1','-0']
df ['Jour'] = Jour
print(df.head())

with plt.style.context('dark_background') :
    plt.plot(df["Jour"], df["tweet_count"], color='blue')
    plt.title("Nombre de Tweet sur les 7 derniers jours contenant le mot : pomme")
    plt.xlabel("Jour précédent la recherche")
    plt.ylabel("Nombre de Tweet")
    plt.show()



"""
