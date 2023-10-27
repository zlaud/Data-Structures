import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        if self.n<1:
            raise IndexError
        rand_ind = random.randint(0, self.n-1)
        x = self.a[self.j % len(self.a)]
        self.a[self.j % len(self.a)] = self.a[(self.j + rand_ind)% len(self.a)]
        self.a[(self.j + rand_ind) % len(self.a)] = x
        return super().remove()




        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''

