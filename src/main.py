from tweet_fetcher import TweetFetcher
from tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"
next = ""

fetcher = TweetFetcher(BASE_URL)
keyword = "macron"
result = fetcher.get_tweet(keyword,True)
print(str(len(result)) + " tweets were retrieved")

fetcher.export(result, keyword)
print(keyword + " tweets have been written to GCS")


