import tweepy
import pandas as pd

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)


df = pd.read_csv('quotes.csv')
print("---Quote---")
print(df.size)
print(df.iloc[16])
for quote in df:
    print(df[quote])

