import requests
import json
from google.cloud import storage
from datetime import date

class TweetCounter:

    TOKEN = "to chage"

    def __init__(self, base_url):
        self.url = base_url

    def make_url(self, keyword):
        url2 = self.url + "counts/recent?query=" + keyword + "&granularity=day"
        #action sur la granularité ?
        return url2

    def count_tweet(self, keyword):
        url2 = self.make_url(keyword)
        result = self.query(url2)
        return result

    def query(self, url2):
        headers = {
        "Authorization": "Bearer " + TweetCounter.TOKEN
        }
        response = requests.get(url2, headers=headers)
        return response.json()

    def make_filename(self, keyword):
        today = date.today()
        today = today.strftime("%Y-%m-%d")
        html_name = "{}/{}/tweets_count.json".format(today, keyword)  # once per day on Gcloud -->date/keyword/tweets
        return html_name

    def export(self, data, keyword):
        data_json = json.dumps(data, indent=4, ensure_ascii=False)
        client = storage.Client()
        bucket = client.get_bucket('tweets-project-esme')  # bucket name -->unique name
        filename = self.make_filename(keyword)
        blob = bucket.blob("tweets/" + filename)
        blob.upload_from_string(data_json)
        print("Export counts to Google Cloud Storage")
