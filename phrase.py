import itertools
			

def read_words(filename):
	words = open(filename, 'r').readlines()
	return filter(lambda x: x !='',map(lambda y: y.strip(),words))
	


def flatten(list):
	new = []
	if list == []:
		return []
	if type(list[0]) == type([]):
			return flatten(list[0]) + flatten(list[1:])
	else:
			return [list[0]] + flatten(list[1:])
			
	

# assumes phone number is a string	
def phrase(phoneNumber, wordList, maxNums):
		
	phrases = []	
	letters = [["0" for x in xrange(4)] for x in xrange(7)]	
	for i in range(0,7):
		if phoneNumber[i] == '2':
			letters[i][0] = 'a'
			letters[i][1] = 'b'
			letters[i][2] = 'c'
		
		if phoneNumber[i] == '3':
			letters[i][0] = 'd'
			letters[i][1] = 'e'
			letters[i][2] = 'f'	
			
		if phoneNumber[i] == '4':
			letters[i][0] = 'g'
			letters[i][1] = 'h'
			letters[i][2] = 'i'
			
		if phoneNumber[i] == '5':
			letters[i][0] = 'j'
			letters[i][1] = 'k'
			letters[i][2] = 'l'

		if phoneNumber[i] == '6':
			letters[i][0] = 'm'
			letters[i][1] = 'n'
			letters[i][2] = 'o'

		if phoneNumber[i] == '7':
			letters[i][0] = 'p'
			letters[i][1] = 'q'
			letters[i][2] = 'r'
			letters[i][3] ='s'
			
		if phoneNumber[i] == '8':
			letters[i][0] = 't'
			letters[i][1] = 'u'
			letters[i][2] = 'v'

		if phoneNumber[i] == '9':
			letters[i][0] = 'w'
			letters[i][1] = 'x'
			letters[i][2] = 'y'
			letters[i][3] = 'z'	

	print "Calculating... please be patient."	
	print "\n"
			
	potentialWords = [[] for x in xrange(7)]		
	
	for l in range(7,0,-1):
			potentialWords[0]+= getPotentialWords(l, letters)
	
	#print potentialWords[0]
	
	for l in range(6,0,-1):
			potentialWords[1]+= getPotentialWords(l, letters[1:])
	
	for l in range(5,0,-1):
			potentialWords[2]+= getPotentialWords(l, letters[2:])
	
	for l in range(4,0,-1):
			potentialWords[3]+= getPotentialWords(l, letters[3:])
	
	for l in range(3,0,-1):
			potentialWords[4]+= getPotentialWords(l, letters[4:])
		
	for l in range(2,0,-1):
			potentialWords[5]+= getPotentialWords(l, letters[5:])

	
	potentialWords[6].append(letters[6][0])
	potentialWords[6].append(letters[6][1])
	potentialWords[6].append(letters[6][2])
	potentialWords[6].append(letters[6][3])
	
	words =[[] for x in xrange(7)] 
	
	for i in range(0,7):
		for w in range(len(potentialWords[i])):
			if potentialWords[i][w] in wordList:
				words[i].append(potentialWords[i][w])

		
	
	
	
	findPhrases(words,phoneNumber, maxNums)
	
	
def getPotentialWords(length, letters):	
	potentialWords = []	
	
	#print letters	
	if length == 1:
		potentialWords.append(letters[0][0])
		potentialWords.append(letters[0][1])
		potentialWords.append(letters[0][2])
		potentialWords.append(letters[0][3])
		return potentialWords

	else:
		for i in range(0,3):
			words = getPotentialWords(length-1,letters)
			for j in range(len(words)):
				potentialWords.append(words[j]+letters[length-1][i])
	
		return potentialWords			


	
	
	
	
def findPhrases(words, number, max):
	
	phrases = []
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	print number
	print "\n"

	words2 = flatten(words)
	for i in range(len(number)):
		words2+= number[i]
	
	index = 0
	newphrases = []
	phrases += words
	phrases += itertools.permutations(words2, 2)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
					
				if word in numbers:
					i = temp.index(word)
					count+= 1
					if number[i] == word:
						index+=1
						
			if index == 6 and count<= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	
	newphrases = []
	
	
	phrases = itertools.permutations(words2, 3)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
				
				if word in numbers:
					count+=1
						
					if number[i] == word:
						index += 1
						
			if index == 6 and count <= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	
	newphrases = []
		


	
	phrases = itertools.permutations(words2, 4)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
					
				if word in numbers:
					count+=1
					if number[i] == word:
						index+=1
						
			if index == 6 and count <= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	
	newphrases = []
		
	phrases = itertools.permutations(words2, 5)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
					
				if word in numbers:
					count+=1
					if number[i] == word:
						index+=1
						
			if index == 6 and count <= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	
	newphrases = []
	
	phrases = itertools.permutations(words2, 6)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
					
				if word in numbers:
					count+=1
					if number[i] == word:
						index+=1
						
			if index == 6 and count <= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	
	newphrases = []
	
	phrases = itertools.permutations(words2, 7)
	for possible in phrases:
		count = 0
		temp = "".join(possible)
		if len(temp) == 7:
			index = 0
			for word in possible:  
				i = temp.index(word)
				
				if word in words[i]:
					if i != 0:
							index+= len(word)-1
					else:
							index+= len(word)
					
				if word in numbers:
					count+=1
					if number[i] == word:
						index+=1
						
			if index == 6 and count <= max:
				if temp not in newphrases:
					newphrases.append(temp)
			
		
	print newphrases
	print "\n"
	





		