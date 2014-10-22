





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
	



