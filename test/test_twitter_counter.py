from src.tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"

def test_make_url_count():
    counter = TweetCounter(BASE_URL)
    url = counter.make_url("macron")
    expected_url = "https://api.twitter.com/2/tweets/counts/recent?query=macron"
    assert url == expected_url

