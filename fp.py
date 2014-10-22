
def ownerify(owner):
	return lambda x: str(owner) + "'s "+ str(x)



#define: fsum= sum of a list of numbers
def fsum(list):
		return reduce(lambda x,y: x+y, list)
			
def fprod(list):

	
	return reduce(lambda x,y: x*y, list)
				
	
def fmax(list):
		
	max = 0
	for i in range(len(list)):
		if (list[i]> max):
			max = list[i]
			
	return max
			
	
def fmin(list):
	min = 1000
	for i in range(len(list)):
		if (list[i]<min):
			min = list[i]
			
	return min
	
def fac(n):
	return fprod(range(1,n+1))
	
		
# Homework.: define fzip
	#fzip(function, list1, list2, ...... list n) 
	#Example: fzip(lambda x: ''.join(x), ["a","b","c"],["d","e","f"]) = ["ad","be","cf"]
	

def fzip(*args):
	
	
	function = args[0]
	funArgs = zip(*args[1:])
	answer = []
	
	for i in range(0,len(funArgs)):
		answer.append(function(funArgs[i]))
	
	print answer
	return answer
	
	

	
	
	
	
	
	
	
	
	