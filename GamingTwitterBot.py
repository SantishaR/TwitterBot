# import packages
import pip
import tweepy
import time

# Authenticate to twitter

consumer_key = 'ZZi35DC4MM5yngE33nY1a2N5x'
consumer_secret = 'K2ISVhhKkpmPF2Rhp1bDcgYewx0SB9yPgZ6JNBicLONol33CUI'
access_key = '1416760234488512515-SLqnlmGB1x404Ea1wNoQyDRZAmInqz'
access_secret = 'gfgO5VPx6bIkksmwl8k7AF6yzP3Z001UJqK2Z361zAQWR'

# Create API object

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'gamingnews'
num_of_tweets = 1000

for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    try:

        tweet.retweet()
        print("Retweet")
        time.sleep(0)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
