import requests
import json
from google.cloud import storage
from datetime import date

class TweetFetcher:
   
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
        return result

    def query(self, url):
        headers = {
        "Authorization": "Bearer " + TweetFetcher.TOKEN
        }
        response = requests.get(url, headers=headers)
        return response.json()

    def make_filename(self,keyword):
        today = date.today()
        today = today.strftime("%Y-%m-%d")
        html_name = "{}/{}/tweets.json".format(today,keyword)  #once per day on Gcloud -->date/keyword/tweets
        return html_name

    def export(self,data,keyword):
        data_json = json.dumps(data, indent=4,ensure_ascii=False)
        client = storage.Client()
        bucket = client.get_bucket('tweets-project-esme') # bucket name -->unique name
        filename = self.make_filename(keyword)
        blob = bucket.blob("tweets/" + filename)
        blob.upload_from_string(data_json)
        print("Export tweets to Google Cloud Storage")




