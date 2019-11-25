from requests_oauthlib import OAuth1Session
import json
import settings

twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

params = {"count":200}
req = twitter.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params = params)

timeline = json.loads(req.text)

for tweet in timeline:
  print(tweet["text"])
