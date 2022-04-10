import requests
import json
import matplotlib.pyplot as plt
import pandas as pd
url = "https://api.twitter.com/2/tweets/search/recent?query=macron -is:retweet"
headers = {
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAACNWaQEAAAAAQaaBxfOjJCX1m3H%2BF0qrSGFIKPc%3DQxdEvIXQi90IT32aQ8JDcOmxgnp34idYC5H712BzQfybgyRv9r"
}

response = requests.get(url, headers=headers)
répertoire=response.json()
#
with open("data_file.json", "w") as write_file:
    json.dump(répertoire, write_file,indent=1,)
#
with open("data_file.json", "r") as read_file:
    RecTweet = json.load(read_file)
#
for key in RecTweet:
     print(json.dumps(RecTweet, indent=4,ensure_ascii=False))
#

comptage = "https://api.twitter.com/2/tweets/counts/recent?query=macron&granularity=day"
Compt = requests.get(comptage, headers=headers)
CompTweet=Compt.json()
print(json.dumps(CompTweet, indent=4,ensure_ascii=False))

for count in CompTweet["data"]:
    print(count)


df = pd.DataFrame(CompTweet["data"])
Jour = ['-7','-6','-5','-4','-3','-2','-1','-0']
df['Jour'] = Jour
print(df.head())

with plt.style.context('dark_background') :
    plt.plot(df["Jour"], df["tweet_count"], color='blue')
    plt.title("Nombre de Tweet sur les 7 derniers jours contenant le mot : macron")
    plt.xlabel("Jour précédent la recherche")
    plt.ylabel("Nombre de Tweet")
    plt.show()




