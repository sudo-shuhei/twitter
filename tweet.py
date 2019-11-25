#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import settings
import generate

s = generate.generate()+" [bot]"
print(s)
# s = input()
twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

params = {"status": s}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json",params = params)
