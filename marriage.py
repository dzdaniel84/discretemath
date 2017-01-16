class Simulation:
	
	def __init__(self, n):
		self.boys = numbers(n)
		self.girls = letters(n)

	def run(self):
		while notOptimal(self):
			[b.propose() for b in self.boys]
			[g.consider() for g in self.girls]
			[b.evaluate() for b in self.boys]

class Person:
	def propose():

	def consider():

	def evaluate():

class Boy(Person):

class Girl(Person):

def numbers(n):

def letters(n):

def notOptimal(sim):