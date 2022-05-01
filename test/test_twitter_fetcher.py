from src.tweet_fetcher import TweetFetcher

BASE_URL = "https://api.twitter.com/2/tweets/"

def test_make_url_with_retweet():
    
    fetcher = TweetFetcher(BASE_URL)
    url = fetcher.make_url("macron", True)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron -is:retweet"
    assert url == expected_url

def test_make_url_without_retweet():
    fetcher = TweetFetcher(BASE_URL)
    url = fetcher.make_url("macron", False)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron"
    assert url == expected_url

