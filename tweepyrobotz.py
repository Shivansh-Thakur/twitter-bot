#You will need to PIP INSTALL tweepy for this to work and also create a twitter API. Run this on your own machine, not in this Repl. 
import tweepy
import time

consumer_key = 'ziV0Y1q6jjqv5pcRlPCEeTaJx'
consumer_secret = 'Bj0M24yk4VKhzt7XcqGiVFVc4Urtsb6Rxr7Rdfn6kEV4NrqS5g'
access_token = 'AAAAAAAAAAAAAAAAAAAAAJpPYwEAAAAAp%2BUiDtle8Qmn6zjfSyldAcDTZCU%3D5dnftB6GO4ILvl13yyYvLuwbsvBTbBSxQx3VgpmV7NOHNB6C1o'
access_token_secret = '1215640503938510848-pqWG7iuBj2VSPAXuu0sQCxD5PWmagf'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name)
print (user.followers_count)

search = "zerotomastery"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)

#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()


# Be a narcisist and love your own tweets. or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break