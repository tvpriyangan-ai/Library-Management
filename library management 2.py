class Library:

    def __init__ (self,booklist,name):
        self.bookList=booklist
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f'We have following books in our library:{self.name}')
        for book in self.bookList:
            print(book)

    def lendBook(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print('Book has been lended. database updated')
        else:
            print(f'Book is already being used by {self.lendDict[book]}')

    def addBook(self,book):
        if book in booksList:
            print('Book already exists')
        else:
            self.bookList.append(book)
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Book added')

    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print('Book returned successfully')
        else:
            print('The book does not exist in the book lending database')







def main():
    while(True):
        print(f'Welcome to the {library.name}library. Following are the options')
        choice='''
            1.Display Books
            2.Lend Book
            3.Add a Book
            4.Return a Book'''

        print(choice)
        
        userInput=input('press Q to quit and C to continue')
        if userInput == 'C':
            userChoice=int(input('Select an option to continue'))
            if userChoice == 1:
                library.displayBooks()
            
            elif userChoice == 2:
                book=input('Enter the name of the book you want to lend:')
                user=input('Enter the name of the user:')
                library.lendBook(book,user)

            elif userChoice == 3:
                book=input('Enter your book name:')
                library.addBook(book)

            elif userChoice==4:
                book=input('Enter your Book name:')
                library.returnBook(book)

            else:
                print('please choose a valid option')

        elif userInput == 'Q':
            break
        else:
            print('Please enter a valid option')


if__name__='__main__'
booksList=[]
databaseName=input('Enter the name of the database file with extenstion')
bookDatabase=open(databaseName,'r+')
for book in bookDatabase:
    booksList.append(book)
library=Library(booksList,'PythonX')
main()






