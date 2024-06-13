#H24121133 統計一 陳星宇
#用tuple存資料在list
lst = []

def printmenu():
    print('Menu:')
    print('1. Add a book')
    print('2. Remove a book')
    print('3. Get book information')
    print('4. List all books')
    print('5. List books by genre')
    print('6. Quit')

def printinf(a,b,c):
    print(a,end = ' (')
    print(b,end = ', $')
    print("%.2f" % float(c),end = ')')
    print('')

def add_book():
    global lst
    print('')
    inf = str(input('Enter the title, genre, and price of the book (separated by |):')).split('|')
    lst.append((inf[0],inf[1],float(inf[2])))
    print('')
    print('Added',inf[0],'to the library.')
    list_all_books()

def remove_book():
    global lst
    n = len(lst)
    name = str(input('Enter the title of the book:'))
    for i in range(n):
        if(lst[i][0] == name):
            del lst[i]
            print('')
            print('Remove',name,'from the library.')
            print('')
            list_all_books()
            return
    print('')
    print('Error:',name,'not found in the library.')

def get_book_info():
    global lst
    print('')
    name = str(input('Enter the title of the book:'))
    for item in lst:
        if(item[0] == name):
            print('Title:',item[0])
            print('Genre:',item[1])
            print('Price:',item[2])
            return
    print('')
    print('Error:',name,'not found in the library.')

def list_all_books():
    print('')
    global lst
    for item in lst:
        printinf(item[0],item[1],item[2])

def list_books_by_genre():
    global lst
    print('')
    genre = str(input('Enter the genre to search for:'))
    for item in lst:
        if(item[1] == genre):
            printinf(item[0],item[1],item[2])
            return
    print('')
    print('No books found in the',genre,'genre.')

while 1:
    printmenu()
    op = int(input('Enter your choice (1-6):'))
    if(op == 1):
        add_book()
    elif(op == 2):
        remove_book()
    elif(op == 3):
        get_book_info()
    elif(op == 4):
        list_all_books()
    elif(op == 5):
        list_books_by_genre()
    elif(op == 6):
        break
    print('')
