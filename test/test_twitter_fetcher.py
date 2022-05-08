from src.tweet_fetcher import TweetFetcher
from datetime import date


BASE_URL = "https://api.twitter.com/2/tweets/"
fetcher = TweetFetcher(BASE_URL)

def test_make_url_with_retweet():
    url = fetcher.make_url("macron", True)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron -is:retweet"
    assert url == expected_url

def test_make_url_without_retweet():
    url = fetcher.make_url("macron", False)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron"
    assert url == expected_url

def test_make_filename():
    filename = fetcher.make_filename("macron")
    today = date.today().strftime("%Y-%m-%d")
    expected_filename = today + "/macron/tweets.json"
    assert filename == expected_filename

def test_add_next_token():
    token = "b26v89c19zqg8o3fpytm9z5420haerh624b3uwz6jo6f1"
    url_with_next_token = fetcher.add_next_token("https://api.twitter.com/2/tweets/search/recent?query=macron", token)
    assert url_with_next_token == "https://api.twitter.com/2/tweets/search/recent?query=macron&next_token=b26v89c19zqg8o3fpytm9z5420haerh624b3uwz6jo6f1"

def test_flatten():
    my_list = [[1, 2, 3], [4, 5, 6]]
    flatten_list = fetcher.flatten(my_list)
    assert flatten_list == [1, 2, 3, 4, 5, 6] 