import tweepy
import yaml

secrets = yaml.load(file('secrets.yml', 'r'))

# print secrets
#
# auth = tweepy.OAuthHandler(secrets['api_key'], secrets['api_secret'])
# auth.set_access_token(secrets['access_token'], secrets['access_secret'])
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()

# for tweet in public_tweets:
#     print tweet.text

class listener(tweepy.StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = tweepy.OAuthHandler(secrets['api_key'], secrets['api_secret'])
auth.set_access_token(secrets['access_token'], secrets['access_secret'])

twitterStream = tweepy.Stream(auth, listener())
twitterStream.filter(track=['jalopnik'])
