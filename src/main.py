from tweet_fetcher import TweetFetcher
from tweet_counter import TweetCounter

BASE_URL = "https://api.twitter.com/2/tweets/"
next =""
fetcher = TweetFetcher(BASE_URL)
result = fetcher.get_tweet("macron",True)
if result.key("next_token") =! None:

    next = next +"&"+ result['meta']['next_token']
    next_fetcher=TweetFetcher(BASE_URL+next)
    next_result = next_fetcher.get_tweet("macron", True)
    fetcher.export(next_result, "macron")

fetcher.export(result,"macron")

# counter = TweetCounter(BASE_URL)
# result2 = counter.count_tweet("macron")
# counter.export(result2)


