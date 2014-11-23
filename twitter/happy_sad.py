from sentiment import *
from operator import itemgetter


def get_stop_words(filename):
	words = open(filename, 'r').readlines()
	stopwords = []
	for stopword in words:
		stopwords.append(stopword.replace('\n', ''))
	return stopwords


#returns a dict of {word : sentiment}
def infer_word_sentiments(codes, text):
	
	inferred_sentiments = {}
	stopwords = get_stop_words("data/stopwords.txt")
	word_count = {}
	
	for t in text:
		words = t.split(' ')
		for w in words:
			if "http" in w or '@' in w or '#' in w or w == '':
				break
				
			if ((w not in stopwords) and (not codes.has_key(w))):
				if not inferred_sentiments.has_key(w):
					inferred_sentiments[w] = sentiment_score(codes, t)
					word_count[w] = 1
				else:
					inferred_sentiments[w] += sentiment_score(codes, t)
					inferred_sentiments[w] /= 2
					word_count[w] += 1
	
		
	return inferred_sentiments, word_count




def infer_tweet_word_sentiments(codes, tweets):
	x=1


def top_n_words(sentiment_score_dict, n, direction =1):
	if direction == 0:	
		return sorted(sentiment_score_dict.items(), key=itemgetter(1))[:n]	
	else:
		return sorted(sentiment_score_dict.items(), key=itemgetter(1), reverse = True)[:n]




def build_word_cloud_list(sentiment_score_dict, n, filename, word_count = 0, direction =1):
	
	top_n = top_n_words(sentiment_score_dict, n, direction)
	
	wfile = open("./" + filename + '.txt', 'w')
	for word in top_n:
		for i in range((int)(abs(word[1])*10) + (word_count[word[0]] * 10)):
			wfile.write(word[0] +" ")
	wfile.write("\n")	
	wfile.close()
	




def score_sentiments(codes, tweets, n, direction = 1, filename = None):
	
	sentiment_codes, word_count = infer_word_sentiments(codes, tweets)
	
	print top_n_words(sentiment_codes, n, direction)
	
	if filename != None:
			build_word_cloud_list(sentiment_codes, n, filename, word_count, direction)









