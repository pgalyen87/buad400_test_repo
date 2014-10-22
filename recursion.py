
def fac(n):
	if n==0:
		return 1
	else:
		return n* fac(n-1)

		
		
		
def rev(list):
	
	list2 = []
	if len(list) == 0:
		return []
	else:	
		list2.append(list[-1])
		list2.extend(rev(list[:-1]))
		return list2
		
		
def rev2(list):
	if len(list) == 0:
		return []
	else:	
		return rev2(list[1:]) + [list[0]]		
		
		
		
def fib(f,s,n):
	if n ==1:
		return f
	elif n==2:
		return s
	else: 
		return fib(f,s,n-1)+fib(f,s,n-2)
		
		
		
def fastFib(f,s,n,cache = {}):
	if cache.has_key(n):
		return cache[n]
	elif n== 1:
		return f
	elif n==2:
		return s
	else:
		cache[n] = fastFib(f,s,n-1,cache) + fastFib(f,s,n-2,cache)
		return cache[n]
		
		
		
		
def flatten(list):
	new = []
	if list == []:
		return []
	if type(list[0]) == type([]):
			return flatten(list[0]) + flatten(list[1:])
	else:
			return [list[0]] + flatten(list[1:])
			
			
	