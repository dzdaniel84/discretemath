import math

def gcd(x, y):
	if y == 0:
		print("Since y = 0, we conclude that the gcd is {}.".format(x))
		return x
	print("Given x = {} and y = {}, we set the new x to be {} and the new y to be {} % {} = {}".format(x, y, y, x, y, x % y))
	return gcd(y, x % y)

def extended_gcd(x, y):
	if y == 0:
		return (x, 1, 0)
	else:
		print("Given x = {} and y = {}, we now calculate extended_gcd on {}, {} % {} = {}\n"\
			.format(x, y, y, x, y, x % y))
		d, a, b = extended_gcd(y, x % y)
		print("We have deduced that d = {}, a = {}, and b = {} for x = {}, y = {}."\
			.format(d, b, a - math.floor(x/y) * b, x, y))
		print("\t{} = {}*{} + {}*{}\n".format(d, a, x, b, y))
		return (d, b, a - math.floor(x/y) * b)