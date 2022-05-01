from tweet_fetcher import TweetFetcher
from tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"

fetcher = TweetFetcher(BASE_URL)
result = fetcher.get_tweet("macron",True)

fetcher.export(result,"macron")

# counter = TweetCounter(BASE_URL)
# result2 = counter.count_tweet("macron")
# counter.export(result2)


