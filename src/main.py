import flask

from tweet_counter import TweetCounter
from tweet_fetcher import TweetFetcher

BASE_URL = "https://api.twitter.com/2/tweets/"

keywords = ["le pen"]

fetcher = TweetFetcher(BASE_URL)
counter = TweetCounter(BASE_URL)


def run_tweets_acquisition(request):
    for keyword in keywords:
        tweets = fetcher.get_tweet(keyword, True, 100)
        duplicates = fetcher.count_duplicates(tweets)
        print("{} tweets have been fetched with {} duplicates".format(len(tweets), duplicates))
        fetcher.export(tweets, keyword)

        counts = counter.count_tweet(keyword)
        counter.export(counts, keyword)
        print(keyword + " counts have been written to GCS")
    flask.Response(status=200)


run_tweets_acquisition(None)
