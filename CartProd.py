
def cart_prod(*args):

	print args[0]
	if len(args)== 0:
		return []
	if len(args)==1:
		return map(lambda x: [x], args[0])
	for item in range(len(args[0])):
		print args[0][item]
		list.append([args[0][item]] + cart_prod(*args[1:]))
	return list

"""

def cart_prod2(*sets):
	if len(sets) == 0:
		return []
	elif len(sets) ==1:
		return map(lambda x: [x],sets[0])
	else:
		rest = cart_prod2(*sets[1:])
		fn = lambda x: map(lambda y: [x] + y, rest)
		return reduce(lambda x,y: x +y, map(fn, sets[0])) 

"""

