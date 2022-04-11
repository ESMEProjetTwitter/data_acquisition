from twitter_fetcher import TwitterFetcher

BASE_URL = "https://api.twitter.com/2/tweets/"

fetcher = TwitterFetcher(BASE_URL)
result = fetcher.get_tweet("macron",True)

fetcher.export(result)

fetcher_count = TwitterFetcher(BASE_URL)
result2 = fetcher.count_tweet("macron")
fetcher.export(result2)
