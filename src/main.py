from tweet_fetcher import TweetFetcher
from tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"

keyword = "macron"

next = ""
fetcher = TweetFetcher(BASE_URL)
result1 = fetcher.get_tweet(keyword,True)
print(str(len(result1)) + " tweets were retrieved")
fetcher.export(result1, keyword)
print(keyword + " tweets have been written to GCS")

counter = TweetCounter(BASE_URL)
result2 = counter.count_tweet(keyword)
counter.export(result2, keyword)
print(keyword + " counts have been written to GCS")


