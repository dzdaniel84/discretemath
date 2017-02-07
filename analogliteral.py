"""
Written by Daniel Zhang on February 6, 2017.

An implementation of this infamous article (http://www.eelis.net/C++/analogliterals.xhtml) in Python.
Import this into all your code for some extra fun :^)
Since idea is not mine, feel free to do whatever with this code if you want.
Only use {'O', 'L', '-', '|'} in your analog literals, please.
"""

def length(str):
	return str.count('-')

def area(str):
	return (str.count('-') * str.count('|')) / 4

def volume(str):
	return (str.count('|') * str.count('-') * str.count('L'))/27

"""
assert(volume("""
O-----------O
|L           L
| L           L
|  L           L
|   L           L
O    O-----------O
 L   |           |
  L  |           |
   L |           |
    L|           |
     O-----------O
""") == 176)

assert(area("""
			 O----O
			 |    |
			 |    |
			 |    |
			 |    |
			 O----O
			 """) == 16)

assert(length("O-----------O" == 11)
""""""