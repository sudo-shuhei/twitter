import pandas as pd
import re
import csv

df = pd.read_csv('tweet.csv')
# print(df.shape)
# print(df.index)
# print(df.columns)
tweets = df["text"]

replypattern = '@[\w]+'
urlpattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
retweet = 'RT.*'

processedtweets = []

for tweet in tweets:
    # print(tweet)
    i = re.sub(replypattern, '', tweet)
    i = re.sub(urlpattern, '', i)
    i = re.sub(retweet, '',i)
    if isinstance(i, str) and not i.split():
        pass
    else:
        processedtweets.append(i)

processedtweetsDataFrame = pd.Series(processedtweets)
newDF = pd.DataFrame({'text': processedtweetsDataFrame})

newDF.to_csv('processedtweets.csv')
