from tweet_fetcher import TweetFetcher
from tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"

keywords = ["macron", "zemmour", "le pen", "mélenchon"]

fetcher = TweetFetcher(BASE_URL)
counter = TweetCounter(BASE_URL)

for keyword in keywords:
    tweets = fetcher.get_tweet(keyword,True)
    print(str(len(tweets)) + " tweets were retrieved")
    fetcher.export(tweets, keyword)
    print(keyword + " tweets have been written to GCS")

    counts = counter.count_tweet(keyword)
    counter.export(counts, keyword)
    print(keyword + " counts have been written to GCS")


