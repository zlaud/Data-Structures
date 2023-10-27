from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        if (0 <= i < self.n) and (0 <= j < self.n):
            self.adj[i][j] = True
        else:
            raise IndexError

    def remove_edge(self, i : int, j : int):
        if (0 <= i < self.n) and (0 <= j < self.n):
            s = self.adj[i][j]
            self.adj[i][j] = False
            return s
        else:
            raise IndexError

    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j]

    def out_edges(self, i) -> List:
        edges = []
        for j in range(len(self.adj[i])):
            if self.adj[i][j] == 1:
                edges.append(j)
        return edges

    def in_edges(self, j) -> List:
        edges = []
        for i in range(len(self.adj[j])):
            if self.adj[i][j] == 1:
                edges.append(i)
        return edges

    def bfs(self, r : int):
        trav = []
        seen = [False]*len(self.adj)
        q = ArrayQueue.ArrayQueue()
        q.add(r)
        trav.append(r)
        seen[r] = True
        while q.size() > 0:
            curr = q.remove()
            neighbors = self.out_edges(curr)
            for j in neighbors:
                if seen[j] is False:
                    q.add(j)
                    trav.append(j)
                    seen[j] = True
        return trav

    def dfs(self, r : int):
        trav = []
        s = ArrayStack.ArrayStack()
        seen = [False]*len(self.adj)
        s.push(r)
        while s.size() > 0:
            curr = s.pop()
            if seen[curr] is False:
                trav.append(curr)
                seen[curr] = True
            neighbors = self.out_edges(curr)
            for j in reversed(neighbors):
                if seen[j] is False:
                    s.push(j)
        return trav

    def size(self):
        return self.n

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s