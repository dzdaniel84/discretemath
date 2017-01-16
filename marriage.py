import random

class Simulation:
	
	def __init__(self, n):
		self.boys, self.girls = numbers(self, n), letters(self, n)
		self.day = 0

	def run(self):
		while notOptimal(self):
			[b.propose() for b in self.boys]
			[g.consider() for g in self.girls]
			self.day += 1

	def rank(self, person):
		if Type(person) == Boy:
			girls = copy(self.girls)
			random.shuffle(girls)
			return girls
		else:
			boys = copy(self.boys)
			random.shuffle(boys)
			return boys

	def find(self, char):
		if ord(char) < 97:
			return self.girls[ord(char)-49]
		return self.boys[ord(char)-97]

class Boy:

	def __init__(self, sim, name):
		self.wishlist = sim.rank(self);

	def propose(self):
		print("{} proposed to {}.".format(self, self.wishlist[0]))
		self.wishlist[0].suitors.append(self)

	def remove(self, other):
		print("{} was removed from {}'s list.".format(other,, self))
		if other == self.wishlist[0]
			self.wishlist.pop(0)

	def __repr__():
		return self.name

class Girl:

	def __init__(self, sim, name):
		self.wishlist = sim.rank(self);
		self.suitors = []

	def consider(self):
		print("Current list of suitors for {}: {}".format(self.suitors, self))
		if len(self.suitors) == 0:
			print("No suitors yet for {}. Moving on.".format(self))
			return
		best_suitor = max([self.wishlist.index(s) for s in self.suitors])
		for s in self.suitors:
			if s != self.suitors[best_suitor]
				s.remove(self)
		print("{} selects {} to move on to the next round.".format(self, self.suitors[best_suitor]))

	def __repr__():
		return self.name

def numbers(sim, n):
	return [Boy(sim, str(i)) for i in range(1, n+1)]

def letters(sim, n):
	return [Girl(sim, chr(i+96)) for i in range(1, n+1)]

def notOptimal(sim):
	True