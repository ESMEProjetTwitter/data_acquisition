from src.twitter_fetcher import TwitterFetcher

def test_make_url_with_retweet():
    BASE_URL = "https://api.twitter.com/2/tweets/"
    fetcher = TwitterFetcher(BASE_URL)
    url = fetcher.make_url("macron", True)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron -is:retweet"
    assert url == expected_url

def test_make_url_without_retweet():
    BASE_URL = "https://api.twitter.com/2/tweets/"
    fetcher = TwitterFetcher(BASE_URL)
    url = fetcher.make_url("macron", False)
    expected_url = "https://api.twitter.com/2/tweets/search/recent?query=macron"
    assert url == expected_url

def test_make_url_count():
    BASE_URL = "https://api.twitter.com/2/tweets/"
    fetcher = TwitterFetcher(BASE_URL)
    url = fetcher.make_url2("macron")
    expected_url = "https://api.twitter.com/2/tweets/counts/recent?query=macron"
    assert url == expected_url

