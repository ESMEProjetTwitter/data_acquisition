import requests
import json

class TweetCounter:

    TOKEN = "AAAAAAAAAAAAAAAAAAAAACNWaQEAAAAAQaaBxfOjJCX1m3H%2BF0qrSGFIKPc%3DQxdEvIXQi90IT32aQ8JDcOmxgnp34idYC5H712BzQfybgyRv9r"

    def __init__(self, base_url):
        self.url = base_url

    def make_url(self, keyword):
        url2 = self.url + "counts/recent?query=" + keyword
        #action sur la granularité ?
        return url2

    def count_tweet(self, keyword):
        url2 = self.make_url(keyword)
        result = self.query(url2)

    def query(self, url2):
        headers = {
        "Authorization": "Bearer " + TweetCounter.TOKEN
        }
        response = requests.get(url2, headers=headers)
        return response.json()

    def export(self, data):
        print("Export counts to Google Cloud Storage")

