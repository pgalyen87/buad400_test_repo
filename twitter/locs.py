from twitter_util import *
from sentiment import *



tweets = read_tweets("tweet_data/10.27.tweets.txt")

for t in tweets:
	try:
		print (text(t,['user','location']))
		
	except:
		print("UNREADABLE")