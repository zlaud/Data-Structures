import BinaryHeap
import Book
import ArrayList
import ArrayQueue
import MaxQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
#import BinaryHeap
#import AdjacencyList
import time

import algorithms


class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart.
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = MaxQueue.MaxQueue()
        #self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()

    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key,
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                #self.bookIndices.add(s.key, self.bookCatalog.size()-1)
                self.sortedTitleIndices.add(s.title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting randomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input:
            i: positive integer
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i
        input:
            i: positive integer
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s} \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt: int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input:
            infix: A string
        '''
        start_time = time.time()
        printed = 0
        n = self.bookCatalog.size()
        for i in range(n):
            book = self.bookCatalog.get(i)
            if infix in book.title:
                print(book)
                printed += 1
            if printed == cnt:
                break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        print(self.shoppingCart.max().title)
        return self.shoppingCart.max().title

    def addBookByKey(self, key):
        start_time = time.time()
        i = self.bookIndices.find(key)
        if i is None:
            return("Book not found...")
        if i >= 0 and i < self.bookCatalog.size():
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            print(f'Added title: {s.title}')
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix):
        start_time = time.time()
        n = len(prefix)
        title = self.sortedTitleIndices.key_finder(prefix).k
        if prefix == '':
            return None
        elif prefix == title[0:n]:
            s = self.bookCatalog.get(self.sortedTitleIndices.key_finder(prefix).v)
            self.shoppingCart.add(s)
            print(f'Added title: {title}')
        else:
            print("Error: Prefix was not found.")
        elapsed_time = time.time() - start_time
        print(f"addBookByPrefix Completed in {elapsed_time} seconds")

    def bestsellers_with(self, infix, structure, n = 0):
        best_sellers = None
        if structure == 1:
            best_sellers = BinarySearchTree.BinarySearchTree()
        elif structure == 2:
            best_sellers = BinaryHeap.BinaryHeap()
        else:
            print("Invalid data structure.")
        if best_sellers is not None:
            if infix == '':
                print("Invalid infix.")
            else:
                start_time = time.time()
                s = self.bookCatalog.size()
                for i in range(s):
                    book = self.bookCatalog.get(i)
                    if infix in book.title:
                        if structure == 1:
                            best_sellers.add(book.rank, book)
                        if structure == 2:
                            if book.rank > 0:
                                book.rank *= -1
                            best_sellers.add(book)


                k = best_sellers.size()-int(n)
                if int(n) > 0:
                    for i in range(best_sellers.size()-1, k-1, -1):
                        if structure == 1:
                            print(best_sellers.in_order()[i].v)
                        if structure == 2:
                            print(best_sellers.remove())
                if int(n) == 0:
                    for i in range(best_sellers.size()-1, -1, -1):
                        if structure == 1:
                            print(best_sellers.in_order()[i].v)
                        if structure == 2:
                            print(best_sellers.remove())
                elapsed_time = time.time() - start_time
                print(f"Displayed bestsellers_with ({infix}, {structure}, {n}) in {elapsed_time} seconds")

    def sort_catalog(self, s: int):
        start_time = time.time()
        if s == 1:
            algorithms.merge_sort(self.bookCatalog)
            return True
        elif s == 2:
            algorithms.quick_sort(self.bookCatalog)
            return True
        elif s == 3:
            algorithms.quick_sort(self.bookCatalog, False)
            return True
        else:
            return False
        elapsed_time = time.time() - start_time
        print(f"Sorted {self.bookCatalog.size()} books in {elapsed_time} seconds.")

    def display_catalog(self, n: int):
        for i in range(n):
            book = self.bookCatalog.get(i)
            print(book)

