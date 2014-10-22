
from recursion import *


def nComb(s, n):
	new= []
	newTwo = []
	results = []
	
	if n == 1:
		return map(lambda x: [x], s)	
	elif n == len(s):
		return s
	else:
		for i in range(len(s[0])):
			results = nComb(s[1:], n-1)
			#print "results"
			#print results
			for j in range(len(results)):
				new.append([s[0]]+ results[j])
			
		new.append(nComb(s[1:],n))
	
	return new



def nComb2(s,n):
		if n == 1:
			return map(lambda x: [x], s)
		elif n==len(s):
			return [s]
		else:
			next_reduct = nComb2(s[1:],n-1)
			return map(lambda x: [s[0]] + x, next_reduct) + nComb2(s[1:],n)
			
			


def  all_perms(item):
	
	comb1 = []
	
	
	for i in range(len(item)):
		
		if len(item) <= 1:
			return item
			
		item2 = list(item)
		item2.remove(item[i])
		
		
		
		print "item 2"
		print item2
		for j in range(len(item2)):
			comb1.append(flatten([item[i]]+ all_perms(item2))) 
		
		
	return comb1
	
	
	
	
	
def interleave_all(item, elements):
		ivs = []
		for i in range(len(elements)+1):
			nxt = list(elements)
			nxt.insert(i, item)
			ivs.append(nxt)
		return ivs			
	
def all_perms2(items):
		if len(items) == 1:
			return [items]
		else:
			rest = all_perms2(items[1:])
			return reduce(lambda x,y: x+y, map(lambda z: interleave_all(items[0],z), rest))
				
				
				
				








		