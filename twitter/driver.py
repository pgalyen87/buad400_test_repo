from twitter_util import *
from sentiment import *



tweets = read_tweets("tweet_data/10.27.tweets.txt")

#reads raw texts
#texts = read_texts("tweet_data/10.27.tweets.txt")

# get the user name of the tweeters
for t in tweets:
	try:
		print (text(t,['user','screen_name']))
	except:
		print "<Cannot Retrieve Screen Name>"
		


codes = get_sentiment_codes("data/AFINN-111.txt")

#for i in codes.items()[0:5]:
#			print i


#for t in tweets[:20]:	
#	print(str(sentiment_score(codes, text(t)))+ ":" +  text(t))	

tweetText = []
for t in tweets:
	tweetText.append(text(t, ['text']))


happiest = top_n_tweets(tweets, codes, 10)
saddest = top_n_tweets(tweets,codes, 10, direction = -1)

print('Happiest tweets')

for t in happiest:
	print(' '+ t)
	
	
print('\n')
print('\n')	
	
print('Saddest tweets')	
for t in saddest:
	print(' '+ t)	
	
			