import math


def bold(str):
    return '\033[1m{}\033[0m'.format(str)

def red(str):
    return '\033[91m{}\033[0m'.format(str)

def extended_gcd(x, y, demo = True):
	if y == 0:
		print("Since y = 0, we conclude that the gcd is {}.".format(x))
		return (x, 1, 0)
	else:
		if demo:
			print("Given x = {} and y = {}, we now calculate extended_gcd on {}, {} % {} = {}"\
				.format(x, y, y, x, y, x % y))
			print("\t{} = {}*{} + {}\n".format(x, x//y, bold(y), red(x % y)))
		d, a, b = extended_gcd(y, x % y)
		a , b = b, a - math.floor(x/y) * b
		if demo:
			print("We have deduced that d = {}, a = {}, and b = {} for x = {}, y = {}."\
				.format(d, a, b, x, y))
			print("\t{} = {}*{} + {}*{}\n".format(d, a, x, b, y))
		return (d, a, b)

def run():
	str = input("Please input x and y (separate with a space): ").split(' ')
	x, y = str[0], str[1]
	extended_gcd(x, y)