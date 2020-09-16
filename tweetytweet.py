import tweepy
import time

# Setup auth to API
auth = tweepy.OAuthHandler('<API key>', '<API secret>')
auth.set_access_token('<Access token>', '<Access secret>')

api = tweepy.API(auth)
user = api.me()

# Handle rate limiting, so not to spam Twitter with API calls. You can use this as a wrapper.
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
    except StopIteration:
        print('done!')


# Liking tweets
search_string = 'python'
numberofTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberofTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


# # Super generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == '<Twitter Name>':
#         follower.follow()
#         break

