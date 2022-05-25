from tweet_counter import TweetCounter
from tweet_fetcher import TweetFetcher

BASE_URL = "https://api.twitter.com/2/tweets/"

keywords = ["macron", "zemmour", "le pen", "mélenchon"]

fetcher = TweetFetcher(BASE_URL)
counter = TweetCounter(BASE_URL)

for keyword in keywords:
    tweets = fetcher.get_tweet(keyword, True)
    duplicates = fetcher.count_duplicates(tweets)
    print("{} tweets have been fetched with {} duplicates".format(len(tweets), duplicates))
    fetcher.export(tweets, keyword)

    counts = counter.count_tweet(keyword)
    counter.export(counts, keyword)
    print(keyword + " counts have been written to GCS")
