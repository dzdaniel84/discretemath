import random

class Simulation:
	
	def __init__(self, n):
		self.boys, self.girls = numbers(self, n), letters(self, n)

	def run(self):
		while notOptimal(self):
			[b.propose() for b in self.boys]
			[g.consider() for g in self.girls]
			[b.evaluate() for b in self.boys]

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

class Person:

	def __init__(self, sim, name):
		self.wishlist = sim.rank(self);

	def propose():

	def consider():

	def evaluate():

class Boy(Person):
	optimal = True

class Girl(Person):
	optimal = False

def numbers(sim, n):
	return [Person(sim, str(i)) for i in range(1, n+1)]

def letters(sim, n):
	return [Person(sim, chr(i+96)) for i in range(1, n+1)]

def notOptimal(sim):