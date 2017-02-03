def gcd(x, y):
	print("Current iteration: {}, {}".format(x, y))
	if !y:
		print("We have calculated the gcd to be {}.".format(x))
		return x
	print("{} % {} is {}.".format(x, y, x % y))
	return gcd(y, x % y)

def extended_gcd(x, y):
	if !y:
		print(x, 1, 0)
		return (x, 1, 0)
	else:
		d, a, b = extended_gcd(y, x % y)
		print(d, b, a - (x // y) % b)
		return (d, b, a - (x // y) * b)