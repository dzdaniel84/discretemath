import random

class Simulation:
	
	def __init__(self, n):
		self.n = n
		self.boys, self.girls = numbers(self, n), letters(self, n)
		[b.createList() for b in self.boys]
		[g.createList() for g in self.girls]
		self.day = 0

	def run(self):
		self.table()
		optimal = True
		while optimal:
			print("\n\n══ Day {} ══".format(self.day))
			[b.propose() for b in self.boys]
			optimal = not all([g.consider() for g in self.girls])
			self.day += 1
		print("\n\n")

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
		self.wishlist = self.sim.rank(self);

	def propose(self):
		print("{} proposed to {}.".format(self, self.wishlist[0]))
		self.wishlist[0].suitors.append(self)

	def remove(self, other):
		print("{} rejects {}.".format(other, self))
		if other == self.wishlist[0]:
			self.wishlist.pop(0)

	def __repr__(self):
		#return " "*(((self.sim.n//10) + 1)-(int(self.name)//10)) + str(self.name)
		return self.name

class Girl:

	def __init__(self, sim, name):
		self.sim, self.name = sim, name
		self.suitors = []

	def createList(self):
		self.wishlist = self.sim.rank(self);

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

def numbers(sim, n):
	return [Boy(sim, str(i)) for i in range(1, n+1)]

def letters(sim, n):
	return [Girl(sim, chr(i+96)) for i in range(1, n+1)]

Simulation(9).run()