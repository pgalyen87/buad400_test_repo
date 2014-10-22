
from recursion import *
import copy



def nComb2(s,n):
		if n == 1:
			return map(lambda x: [x], s)
		elif n==len(s):
			return [s]
		else:
			next_reduct = nComb2(s[1:],n-1)
			return map(lambda x: [s[0]] + x, next_reduct) + nComb2(s[1:],n)
			


def powerset(list):
	
	ps = [[]]
	
	total = len(list)
	for i in range(1,total+1):
		ps.append(nComb2(list, i))
		
	return ps
	

	
	
def powerset2(item):
	new = []
	 
	if item == None:
		return []
	 
	if len(item) == 1:
		return [item]	 
	
	new.append(flatten(item))
	 
	for i in range(len(item)):
		item2 = []
		item2 = copy.deepcopy(item)
		item2.remove(item[i])
		ans = powerset2(item2)
		for j in range(len(ans)):
			if ans[j] not in new: 
				new.append(ans[j])
	 
	return new	


