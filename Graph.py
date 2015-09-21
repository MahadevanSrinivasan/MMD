import numpy as np
import fractions

class Graph:
  
  def __init__(self):
    self.vertices = []
    self.edges = {}  
  
  def addVertex(self, v):
    if(v not in self.vertices):
      self.vertices.append(v)

  def addEdge(self, b, a):
    if(b not in self.edges):
      self.edges[b] = [a]
    else:
      self.edges[b].append(a)


  def printEdges(self):
    for k in self.edges.keys():
      print k, self.edges[k]
  
  def createAdjMatrix(self):
    n = len(self.vertices)
    M = np.zeros((n, n))
    for i, v in enumerate(self.vertices):
      for k in self.edges[v]:
        j = self.vertices.index(k)
        M[j, i] = 1.0/len(self.edges[v])

    return M

  def powerIterate(self, M, r, iterations, b=1):
    M = M * b
    n = len(self.vertices)
    N = (1-b)*np.ones((n, n))/3.0
    M = M + N
    for i in range(iterations):
      r = np.dot(M, r)
      print "Iteration " + str(i) + ': ',
      for elem in r:
        print str(fractions.Fraction.from_float(elem)) + ' ', 
      print ""



if __name__ == '__main__':
  g = Graph()
  g.addVertex('A')
  g.addVertex('B')
  g.addVertex('C')
  g.addEdge('A', 'C')
  g.addEdge('A', 'B')
  g.addEdge('C', 'A')
  g.addEdge('B', 'C')
  g.printEdges()
  print g.vertices
  M = g.createAdjMatrix()
  print M
  g.powerIterate(M, np.ones(3), 5)
