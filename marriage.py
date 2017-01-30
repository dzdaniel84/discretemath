import random

class Simulation:
	
	def __init__(self, arg):
		if type(arg) == int:
			self.n = arg
			self.boys, self.girls = numbers(self, self.n), letters(self, self.n)
			[b.createList() for b in self.boys]
			[g.createList() for g in self.girls]
			self.day = 0
		else:
			with open(arg, 'r') as f:
				self.n = int(f.readline())
				self.boys, self.girls = numbers(self, self.n), letters(self, self.n)
				for b in self.boys:
					b.parseList(f.readline())
				for g in self.girls:
					g.parseList(f.readline())
				self.day = 0

	def run(self):
		self.table()
		optimal = True
		while optimal:
			print("\n\n══ Day {} ══".format(self.day))
			[b.propose() for b in self.boys]
			optimal = not all([g.consider() for g in self.girls])
			self.day += 1
			for boy in self.boys:
				print(boy.print_status())
		print("\n\nWe have reached a stable configuration, since all males and all females have been paired. " + \
			"These are the final pairings: \n" + "\n".join(["{} and {}".format(g, g.suitors[0]) for g in self.girls]) + "\n\n")

	def rank(self, person):
		if type(person) == Boy:
			girls = self.girls[:]
			random.shuffle(girls)
			return girls
		else:
			boys = self.boys[:]
			random.shuffle(boys)
			return boys

	def find(self, char):
		if ord(char) < 97:
			return self.girls[ord(char)-49]
		return self.boys[ord(char)-97]

	def table(self):
		l = (self.n//10) + 1
		print("╔═════╦╦══" + "══╦══".join('═'*l for i in range(self.n)) + "══╗\t\t" + \
			"╔═════╦╦══" + "══╦══".join('═'*l for i in range(self.n)) + "══╗")
		for i in range(self.n):
			print("║  {}  ║║".format(self.boys[i]) + "║".join("  {}  ".format(g.__repr__()) for g in self.boys[i].wishlist) + "║" \
			+ "\t\t" + "║  {}  ║║".format(self.girls[i]) + "║".join("  {}  ".format(b.__repr__()) for b in self.girls[i].wishlist) + "║")
		print("╚═════╩╩══" + "══╩══".join('═'*l for i in range(self.n)) + "══╝\t\t" + \
			"╚═════╩╩══" + "══╩══".join('═'*l for i in range(self.n)) + "══╝")

class Boy:

	def __init__(self, sim, name):
		self.sim, self.name = sim, name

	def createList(self):
		self.wishlist = self.sim.rank(self)
		self.oldlist = self.wishlist[:]

	def parseList(self, line):
		self.wishlist = []
		line = line.split(' ')[1:self.sim.n+1]
		for girl in line:
			self.wishlist.append(self.sim.find(girl))
		self.oldlist = self.wishlist[:]

	def propose(self):
		print("{} proposed to {}.".format(self, self.wishlist[0]))
		self.wishlist[0].suitors.append(self)

	def remove(self, other):
		print("{} rejects {}.".format(other, self))
		if other == self.wishlist[0]:
			self.wishlist.pop(0)

	def print_status(self):
		lst = repr(self) + ":\t"
		for girl in self.oldlist:
			if girl not in self.wishlist:
				lst += red(girl) + " "
			elif girl == self.wishlist[0]:
				lst += bold(girl) + " "
			else:
				lst += repr(girl) + " "
		return lst

	def __repr__(self):
		return self.name

class Girl:

	def __init__(self, sim, name):
		self.sim, self.name = sim, name
		self.suitors = []

	def createList(self):
		self.wishlist = self.sim.rank(self);
		self.oldlist = self.wishlist[:]

	def parseList(self, line):
		self.wishlist = []
		line = line.split(' ')[1:self.sim.n+1]
		for boy in line:
			self.wishlist.append(self.sim.find(boy))
		self.oldlist = self.wishlist[:]

	def consider(self):
		if len(self.suitors) == 0:
			print("No suitors yet for {}. Moving on.".format(self))
			return False
		best_suitor = max(self.suitors, key = lambda suitor: self.wishlist.index(suitor)) #can simplify more
		for suitor in self.suitors:
			if suitor is not best_suitor:
				suitor.remove(self)
		self.suitors = [best_suitor]
		print("{} tells {} 'Maybe'.".format(self, best_suitor))
		return True

	def __repr__(self):
		return self.name

def bold(str):
    return '\033[1m{}\033[0m'.format(str)

def red(str):
    return '\033[91m{}\033[0m'.format(str)

def numbers(sim, n):
	return [Boy(sim, str(i)) for i in range(1, n+1)]

def letters(sim, n):
	return [Girl(sim, chr(i+96)) for i in range(1, n+1)]

def run():
	print(chr(27) + "[2J")
	while True:
		c = input("Do you have a text file to run? (Y/n) " + bold('> '))
		if (c == 'y' or c == 'Y'):
			c = input("Please enter the location of the file here: " + bold('> '))
			Simulation(c).run()
		else:
			c = input("How many boys/girls do you want paired up? " + bold('> '))
			Simulation(int(c)).run()
	c = input("Simulation terminated. Please press any key to continue.\n")
	print(chr(27) + "[2J")

run()