'''
To run, type 'python3 eulertour.py  > g.dot && dot -Tsvg g.dot -o g.svg && open -a "Google Chrome" g.svg'
in Terminal
'''

"""
To do list:
#Split display code and generate code for each graph
#Create a splice algorithm
#Create a tour algorithm
#Animate GIF of Eulerian tour algorithm
"""

import random

class Node:
    
    def __init__(self, name, graph):
        self.adj = []
        self.name, self.graph = name, graph
        
    def __repr__(self):
        return str(self.name)
        
    @property
    def degree(self):
        return len(self.adj)
    
class Graph:

   #N = number of nodes
   def __init__(self, N):
       self.N = N
       self.nodes = [Node(i, self) for i in range(N)]
   
   def get_node(self, i):
       return self.nodes[i]
   
   def add_edge(self, node1, node2):
       node1.adj.append(node2)
       node2.adj.append(node1)
   
   def exists_edge(self, node1, node2):
       return node1 in node2.adj
   
   def remove_edge(self, node1, node2):
       node1.adj.remove(node2)
       node2.adj.remove(node1)

   def __repr__(self):
       return ' '.join(str(n.degree) for n in self.nodes) + "\n" + \
       '\n'.join([str(n.name) + ":\t" + " ".join([str(c.name) for c in n.adj]) for n in self.nodes])

def generate_dot(g):
  s = 'graph g {\n'
  for node in g.nodes:
    s += "" + str(node.name) + ';\n'
  for node in g.nodes:
    for n2 in node.adj:
      if node.name < n2.name:
        s += "" + str(node.name) + ' -- ' + str(n2.name) + ';\n'
  s += '\n}\n'
  return s
        
def generate(n):
  g = Graph(n)
  
  #This makes sure all nodes have degree greater than 2
  def sparse():
    for node in g.nodes:
        if node.degree < 2:
            return True
    return False
      
  def all_even():
    for node in g.nodes:
        if node.degree % 2:
            return False
    return True
      
  def find_odd_nodes():
    n1, n2 = None, None
    for node in g.nodes:
        if n1 is None and node.degree % 2:
            n1 = node
        elif n2 is None and node.degree % 2:
            n2 = node
    return n1, n2
  
  while sparse():
    i1, i2 = random.randrange(n), random.randrange(n)
    n1, n2 = g.get_node(i1), g.get_node(i2)
    if i1 != i2 and not g.exists_edge(n1, n2):
        g.add_edge(n1, n2)
          
  while not all_even():
    n1, n2 = find_odd_nodes()
    if g.exists_edge(n1, n2):
      g.remove_edge(n1, n2)
    else:
      g.add_edge(n1, n2)

  return g

print(generate_dot(generate(100)))