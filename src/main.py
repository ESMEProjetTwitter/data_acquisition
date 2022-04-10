from twitter_fetcher import TwitterFetcher

BASE_URL = "https://api.twitter.com/2/tweets/"

fetcher = TwitterFetcher(BASE_URL)
result = fetcher.get_tweet("macron",True)

fetcher.export(result)
