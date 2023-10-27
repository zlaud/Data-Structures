import BookStore
import Calculator
import DLList
import AdjacencyMatrix




def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression 
        2 Store variable values
        3 Print expression with values
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        elif option == "2":
            decision = ''
            while decision != "N":
                k = input("Enter a variable: ")
                v = float(input("Enter its value: "))
                calculator.set_variable(k,v)
                decision = input("Enter another variable? Y/N ")
        elif option == "3":
            expr = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expr):
                calculator.print_expression(expr)
            else:
                print("Invalid expression")
        elif option == "4":
            expr = input("Enter the expression: ")
            try:
                print(f"Evaluating expression: {calculator.print_expression(expr)}")
                print(f"Result:{calculator.evaluate(expr)}")
                break
            except ValueError:
                print("Result: Error - Not all variable values are defined.")

        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        10 Sort the catalog
        11 Display the first n books of catalog
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            print('getCartBestSeller returned')
            bookStore.getCartBestSeller()
        elif option == "7":
            key = input("Enter book key: ")
            bookStore.addBookByKey(key)
        elif option == "8":
            prefix = input("Introduce the prefix: ")
            bookStore.addBookByPrefix(prefix)
        elif option == "9":
            infix = input("Enter infix: ")
            structure = int(input("Enter structure (1 or 2): "))
            max_titles = input("Enter max number of titles: ")
            bookStore.bestsellers_with(infix, structure, max_titles)
        elif option == "10":
            print("""
                    Choose an algorithm:
                    1 - Merge Sort
                    2 - Quick Sort (first element pivot)
                    3 - Quick Sort (random element pivot)
                    """)
            alg = int(input("Your selection: "))
            if alg == 1 or alg == 2 or alg == 3:
                bookStore.sort_catalog(alg)
            else:
                print("Invalid algorithm")
        elif option == "11":
            n = int(input("Enter the number of books to display: "))
            bookStore.display_catalog(n)



        ''' 
        Add the menu options when needed
        '''

def menu_palindrome():
    list = DLList.DLList()
    pal_word = input("Enter a word/phrase: ").lower()
    s = ''.join(filter(str.isalnum, pal_word))
    cnt = 0
    for i in s:
        list.add(cnt,i)
        cnt += 1
    if list.isPalindrome():
        print("Result: Palindrome")
    else:
        print("Result: Not a palindrome")

# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            menu_palindrome()


if __name__ == "__main__":
    #main()
    s = AdjacencyMatrix.AdjacencyMatrix(5)
    s.add_edge(0,1)
    s.add_edge(0,2)
    s.add_edge(1,3)
    print(s.bfs(0))
    print(s)
































