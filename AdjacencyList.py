"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if (0 <= i < self.n) and (0 <= j < self.n):
            if j not in self.adj[i]:
               self.adj[i].append(j)
        else:
            raise IndexError

    def remove_edge(self, i : int, j : int):
        if (0 <= i < self.n) and (0 <= j < self.n):
            for k in range(len(self.adj[i])):
                if self.adj[i].get(k) == j:
                    self.adj[i].remove(k)
                    return True
            return False
        else:
            raise IndexError

    def has_edge(self, i : int, j: int) ->bool:
        if (0 <= i < self.n) and (0 <= j < self.n):
            for k in self.adj[i]:
                if k == j:
                    return True
            return False
        else:
            raise IndexError

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = []
        for j in range(self.n):
            if self.has_edge(j, i):
                out.append(j)
        return out

    def bfs(self, r : int):
        trav = []
        seen = [False] * len(self.adj)
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
        seen = [False] * len(self.adj)
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

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s
