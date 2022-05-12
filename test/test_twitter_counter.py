from src.tweet_counter import TweetCounter
from datetime import date

BASE_URL = "https://api.twitter.com/2/tweets/"
counter = TweetCounter(BASE_URL)

def test_make_url_count():
    url = counter.make_url("macron")
    expected_url = "https://api.twitter.com/2/tweets/counts/recent?query=macron&granularity=hour"
    assert url == expected_url

def test_make_filename():
    filename = counter.make_filename("macron")
    today = date.today().strftime("%Y-%m-%d")
    expected_filename = today + "/macron/tweets_count.json"
    assert filename == expected_filename

