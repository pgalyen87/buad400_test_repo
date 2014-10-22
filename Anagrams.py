"""
def isAnagram(word1,word2):
	if len(word1)!= len(word2):
		return False
	
	wordlist = []
	
	for i in range(len(word2)):
		wordlist.append(word2[i])
	
	for i in range(len(word1)):
		if word1[i] in wordlist:
			wordlist.remove(word1[i])
	
	if len(wordlist)== 0:
		return True
	else:
		return  False
		
"""		
		
def anagrams(word, word_list):
	hist = word_histogram(word)
	found = []
	for w in word_list:
		if hist == word_histogram(w):
			found.append(w)
	return found		
		

def word_histogram(word):
	hist = {}
	for char in word:
		if not(hist.has_key(char)):
			hist[char] = 1
		else:
			hist[char] += 1
	return hist		

def Anagrams(word, word_list):
	found = []
	for w in word_list:
		if isAnagram(word,w):
			found.append(w)
	
	return found	


	
def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x !='',map(lambda y: y.strip(),words))
	
	
		
	
	