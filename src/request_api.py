import requests

url = "https://api.twitter.com/2/tweets/search/recent?query=pomme -is:retweet"
headers = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACNWaQEAAAAAQaaBxfOjJCX1m3H%2BF0qrSGFIKPc%3DQxdEvIXQi90IT32aQ8JDcOmxgnp34idYC5H712BzQfybgyRv9r"
}

response = requests.get(url, headers = headers)