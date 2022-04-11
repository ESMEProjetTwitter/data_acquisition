import requests
import json

class TwitterFetcher:
   
    TOKEN = "AAAAAAAAAAAAAAAAAAAAACNWaQEAAAAAQaaBxfOjJCX1m3H%2BF0qrSGFIKPc%3DQxdEvIXQi90IT32aQ8JDcOmxgnp34idYC5H712BzQfybgyRv9r"

    def __init__(self, base_url):
        self.url = base_url

    def make_url(self, keyword, retweet):
        url = self.url + "search/recent?query=" + keyword 
        if retweet == True :
            url = url + " -is:retweet"
        return url

    def get_tweet(self, keyword, retweet):
        url = self.make_url(keyword, retweet)
        result = self.query(url)

    def query(self, url):
        headers = {
        "Authorization": "Bearer " + TwitterFetcher.TOKEN
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def export(self, data):
        print("Export to Google Cloud Storage")
######################################################################
    def make_url2(self, keyword):
        url2 = self.url + "counts/recent?query=" + keyword
        #action sur la granularité ?
        return url2

    def count_tweet(self, keyword):
        url2 = self.make_url(keyword)
        result = self.query(url2)

    def query2(self, url2):
        headers = {
        "Authorization": "Bearer " + TwitterFetcher.TOKEN
        }
        response = requests.get(url2, headers=headers)
        return response.json()

