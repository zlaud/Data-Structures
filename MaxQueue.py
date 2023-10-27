from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList


    def add(self, x: object):
        u = self.Node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1

        if self.max_deque.n == 0:
            self.max_deque.add_first(x)

        elif x > self.max_deque.get(0):
            for i in range(self.max_deque.n):
                self.max_deque.remove(0)
            self.max_deque.add_first(x)


        elif self.max_deque.get(0) > x:
            for i in range(self.max_deque.n):
                if x > self.max_deque.get(i):
                    self.max_deque.add(i, x)
                    while self.max_deque.n > i+1:
                        self.max_deque.remove_last()
                    break
                elif x < self.max_deque.get(self.max_deque.n -1):
                    self.max_deque.add_last(x)


    def remove(self) -> object:
        if self.n <= 0:
            raise IndexError
        if self.n == 0:
            return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        if x == self.max_deque.get(0):
            self.max_deque.remove_first()
        return x

        """
        removes and returns the element at the head of the max queue
        """


    def max(self):
        """
        returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)


