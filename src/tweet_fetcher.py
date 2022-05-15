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

    def add_next_token(self, url, token):
        url = url + "&next_token=" + token
        return url

    def get_tweet(self, keyword, retweet):
        url = self.make_url(keyword, retweet)
        result = self.query(url)
        return result

    def flatten(self, results2d):
        flat_list = []
        for sublist in results2d:
            for item in sublist:
                flat_list.append(item)
        return flat_list

    def query(self, url):
        headers = {
        "Authorization": "Bearer " + TweetFetcher.TOKEN
        }
        next_token = None
        all_tweets = []
        response = requests.get(url, headers=headers)
        all_tweets.append(response.json()["data"])
        next_token = response.json()['meta']['next_token']
        # Make the query for page 2 to 100 of the API
        for page_num in range(1, 2):
            if next_token is not None:
                url_with_next_token = self.add_next_token(url, next_token)
                response = requests.get(url_with_next_token, headers=headers)
                all_tweets.append(response.json()["data"])
        return self.flatten(all_tweets)

    def make_filename(self,keyword):
        today = date.today()
        today = today.strftime("%Y-%m-%d")
        html_name = "{}/{}/tweets.json".format(today,keyword)  #once per day on Gcloud -->date/keyword/tweets
        return html_name

    def export(self,data,keyword):
        data_json = json.dumps(data, indent=4,ensure_ascii=False)
        print(data)
        client = storage.Client()
        bucket = client.get_bucket('tweets-project-esme') # bucket name -->unique name
        filename = self.make_filename(keyword)
        blob = bucket.blob("tweets/" + filename)
        blob.upload_from_string(data_json)
        print("Export tweets to Google Cloud Storage")

    def make_unicode(input): #to modify a str to unicode
        if type(input) != "unicode":
            input = input.decode('utf-8')
            return input
        else:
            return input




