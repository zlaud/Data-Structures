import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2*i+1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2*(i+1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i-1)//2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            print("Can not remove from an empty heap.")
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self._trickle_down_root()
        if 3*self.n < len(self.a):
            self._resize()
        return x

    def depth(self, i) -> int:
        d = 0
        for ind in range(self.n):
            if i == self.a[ind]:
                i = ind
        if i > self.n-1:
            return (f'{i} is not found in the binary tree.')
        while i != 0:
            i = parent(i)
            d += 1
        return d

    def height(self) -> int:
        h = math.log2(self.n)
        h = int(h)
        return h

    def bf_order(self) -> list:
        return self

    def in_order(self) -> list:
        return self._in_order(0)

    def _in_order(self, i) -> list:
        inord = []
        if left(i) < self.n:
            inord.extend(self._in_order(left(i)))
        inord.append(self.a[i])
        if right(i) < self.n:
            inord.extend((self._in_order(right(i))))
        return inord


    def post_order(self) -> list:
        return self._post_order(0)

    def _post_order(self, i):
        post = []
        if left(i) < self.n:
            post.extend((self._post_order(left(i))))
        if right(i) < self.n:
            post.extend((self._post_order(right(i))))
        post.append(self.a[i])
        return post

    def pre_order(self) -> list:
        return self._pre_order(0)

    def _pre_order(self, i):
        pre = []
        pre.append(self.a[i])
        if left(i) < self.n:
            pre.extend((self._pre_order(left(i))))
        if right(i) < self.n:
            pre.extend((self._pre_order(right(i))))
        return pre

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n-1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            x = self.a[i]
            self.a[i] = self.a[p_idx]
            self.a[p_idx] = x
            i = p_idx
            p_idx = parent(i)


    def _resize(self):
        b = _new_array(max(1, 2 * self.n))
        for k in range(0, self.n):
            b[k] = self.a[k]
        self.a = b
        return self.a

    def _trickle_down_root(self):
        i = 0
        while i >= 0:
            r_idx = right(i)
            min_idx = -1
            if r_idx < self.n and self.a[r_idx] < self.a[i]:
                l_idx = left(i)
                if self.a[l_idx] < self.a[r_idx]:
                    min_idx = l_idx
                else:
                    min_idx = r_idx
            else:
                l_idx = left(i)
                if l_idx < self.n and self.a[l_idx] < self.a[i]:
                    min_idx = l_idx
            if min_idx >= 0:
                self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]
            i = min_idx


    def __str__(self):
        return str(self.a[0:self.n])