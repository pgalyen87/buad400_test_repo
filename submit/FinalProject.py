import tweepy
from twitter_util import read_props
from sentiment import *
from operator import itemgetter
import matplotlib.pyplot as plt



	

def get_user_names(api):	
	count = 0
	users = []
	
	for tweet in tweepy.Cursor(api.search,
								q="google",
								rpp=100,
								result_type="recent",
								include_entities=True,
								lang="en").items():
		

		
		
		try:
			count += 1
			users.append(str(tweet.user.screen_name))
			if count == 50:
				return users
		except: 
			print('bad text')
			
			

			
			
def get_all_words(api, screen_name):

	codes = get_sentiment_codes("data/AFINN-111.txt")
	#user_sentiment =0
	tweets = []
	count = 0
	temp = []
	
	timeline = api.user_timeline(screen_name)
	for t in timeline:	
		score = sentiment_score(codes, t.text)
		#user_sentiment += score
		if score != 0:
			count += 1
		temp = t.text.split(' ')
		tweets.append(temp)
		
	#print "In function"	
	#print tweets
		
	return tweets, count

	
			
def get_user_sentiment(api, screen_name = 'GummyWormz87'):
	page_list = []
	n = 0
	timeline = api.user_timeline(screen_name)
	tweets = []
	codes = get_sentiment_codes("data/AFINN-111.txt")
	user_sentiment = 0
	count = 0	
	
	
	tweets, count = get_all_words(api, screen_name)
	
	
	for t in tweets:
		tweet = ''
		for w in t:
			tweet = w+' '
		
		score = sentiment_score(codes, tweet)
		user_sentiment += score
	
	if count !=0:
		return (user_sentiment/count)
	else:
		return 0
	
	

def	get_top_n_words(api, screen_name, n = 10, direction = 1):	
	
	count =0
	words, count= get_all_words(api, screen_name)
	
	#print words
	wordcount = {}
	
	
	for word in words:
		#print word
		for w in word:
			#print w
			if wordcount.has_key(w):
				wordcount[w] += 1
			else:
				wordcount[w] = 1
	
	#print wordcount
	
	if direction == 0:	
		return sorted(wordcount.items(), key=itemgetter(1))[:n]	
	else:
		return sorted(wordcount.items(), key=itemgetter(1), reverse = True)[:n]
	
	

def main():		

	props = read_props('secret_account_info.txt')

	consumer_key = props['consumer_key']
	consumer_secret = props['consumer_secret']
	access_token = props['access_token']
	access_token_secret = props['access_token_secret']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)
	
	
	user_names = get_user_names(api)		
	print user_names[:5]
	print "\n"
	
	users = {}
	user_words = {}
	
	for name in user_names:
		users[name] = get_user_sentiment(api, name)
		user_words[name] = get_top_n_words(api, name)
		#print words
	
	print user_names[0]
	print users[user_names[0]]
	print user_words[user_names[0]]
	#print user_words[user_names[0]]
	high = []
	low = []
	#print "made it here"
	
	#try:
	for name in user_names:
		#print users[name]
		if users[name] > 0.5:
			high.append(name)
			#print "HEREE"
		if users[name] < -0.5:	
			low.append(name)
	
	seen = []	
	common_happy = []
	for h in high:
		for word in user_words[h]:
			if word in seen:
				common_happy.append(word)
			else:
				seen.append(word)
				

	"""			
	seen2 = []	
	common_sad = []
	
	for l in low:
		for word in user_words[l]:
			if word in seen:
				common_sad.append(word)
			else:
				seen2.append(word)			
				

	xs = []
	ys = []
	for ch in common_happy:
		xs += common_happy[ch][0]
		ys += common_happy[ch][1]
	"""
	
	print "Common Happy Words"
	print common_happy

	#plt.scatter(xs, ys)
	#plt.show()
	
	#print "\n"
	#print "Common Unhappy Words"
	#print common_sad
	
	
main()	
