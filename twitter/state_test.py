from sentiment import *
from twitter_util import *



tweets = read_tweets("tweet_data/10.27.tweets.txt")

#coded_states
states = read_states("data/states.txt")

#sentiment_codes
codes = get_sentiment_codes("data/AFINN-111.txt")

#for t in tweets:
#	try:
		#print (extract_state(states, text(t,['user','location'])))
#	except:
#		print "UREADABLE"

		
		
		
print top_n_states(states, codes , tweets) 	
		