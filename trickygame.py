head = 'H'
tail = '\033[91mT\033[0m'

def flip(side):
	return tail if side == head else head

def conv(i):
	return ord(i) - 65

class Table:
	def __init__(self, n):
		self.n = n
		self.table = [[head for col in range(n)] for row in range(n)]

	def print(self):
		for t in self.table:
			print(' '.join(i for i in t))

	def flip_row(self, row):
		self.table[int(row)-1] = [flip(coin) for coin in self.table[int(row)-1]]

	def flip_col(self, col):
		for row in self.table:
			row[conv(col)] = flip(row[conv(col)])

def run():
	table = Table(int(input("Input n.\n> ")))
	table.print()

	while(True):
		try:
			query = input("\nWhat would you like to flip?\n> ")
			if ord(query) < 65:
				assert int(query) <= table.n
				table.flip_row(query)
			else:
				assert conv(query) < table.n
				table.flip_col(query)
			table.print()
		except AssertionError:
			print("Error: Input out of bounds.")
		except TypeError:
			print("Error: Wrong type of input.")

run()