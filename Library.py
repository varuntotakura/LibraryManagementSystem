import sys

class Library:
    def __init__(self, bookid, booktitle, author, subject, availablebooks):
        self.bookid = bookid
        self.booktitle = booktitle
        self.author = author
        self.subject = subject
        self.availablebooks = availablebooks

    def displayAvailablebooks(self, arr):
        print("The books we have in our library are as follows:")
        print("================================")
        self.listofbooks = arr
        print("bookid, booktitle, author, subject, no. availablebooks")
        for i in range(len(self.listofbooks)):
            print(self.listofbooks[i].bookid, self.listofbooks[i].booktitle, self.listofbooks[i].author, self.listofbooks[i].subject, self.listofbooks[i].availablebooks)

    def lendBook(self, requestedBookid):
        self.ids = [self.listofbooks[i].bookid for i in range(len(self.listofbooks))]
        if requestedBookid in self.ids:
            if self.listofbooks[requestedBookid].availablebooks > 0:
                print("The book you requested has now been borrowed")
                self.listofbooks[requestedBookid-1].availablebooks -= 1
            else:
                print("Sorry the book you have requested is currently not available")
        else:
            print("Sorry the book you have requested is currently not in the library")
                  
    def addreturnBook(self, returnedBookid):
        if returnedBookid in self.ids:
            self.listofbooks[returnedBookid-1].availablebooks += 1
            print("Thanks for returning your borrowed book")
        else:
            print("Sorry the book you have requested is currently not in the library")

    def searchDisplay(self, arr):
        self.listofbooks = arr
        sub = input("Please enter the subject: ")
        for i in range(len(self.listofbooks)):
            if self.listofbooks[i].subject == sub:
                print(self.listofbooks[i].bookid, self.listofbooks[i].booktitle, self.listofbooks[i].author, self.listofbooks[i].subject, self.listofbooks[i].availablebooks)

class Librarian:
    def __init__(self, arr):
        self.listofbooks = arr

    def addBook(self):
        print("Enter the details of the book you'd like to add>>")
        self.ids = [self.listofbooks[i].bookid for i in range(len(self.listofbooks))]
        self.bookid = int(input("ID: "))
        if self.bookid in self.ids:
            print("Book already available")
            return
        self.booktitle = input("Book Title: ")
        self.author = input("Author Name: ")
        self.subject = input("Subject Name: ")
        self.availablebooks = int(input("No of Books: "))
        return Library(self.bookid, self.booktitle, self.author, self.subject, self.availablebooks)
    
    def modifyBook(self):
        print("Enter the details of the book you'd like to modify>>")
        self.ids = [self.listofbooks[i].bookid for i in range(len(self.listofbooks))]
        self.bookid = int(input("Book ID: "))
        if self.bookid in self.ids:
            bid = self.ids.index(self.bookid)
            self.listofbooks[bid].booktitle = input("Book Title: ")
            self.listofbooks[bid].author = input("Author Name: ")
            self.listofbooks[bid].subject = input("Subject Name: ")
            self.listofbooks[bid].availablebooks = int(input("No. of Books: "))
        else:
            print("Sorry the book you have requested is currently not in the library")
        return

    def deleteBook(self):
        print("Enter the id of the book you'd like to delete>>")
        self.bookid = int(input())
        self.ids = [self.listofbooks[i].bookid for i in range(len(self.listofbooks))]
        if self.bookid in self.ids:
            self.listofbooks.remove(self.listofbooks[self.bookid-1])
        return

class Student:
    def __init__(self, arr):
        self.listofbooks = arr

    def requestBook(self):
        print("Enter the id of the book you'd like to borrow>>")
        self.bookid=int(input())
        return self.bookid

    def returnBook(self):
        print("Enter the id of the book you'd like to return>>")
        self.bookid=int(input())
        return self.bookid

def main():
    library = Library("ID", "Title", "Author", "Subject", "Availability")
    bookids = [1, 2, 3]
    books = ["The Last Battle", "The Screwtape letters","The Great Divorce"]
    authors = ["A", "B", "C"]
    subjects = ["Gen", "Gen", "Law"]
    availablebooks = [3, 6, 9]
    arr = []
    for i in range(len(bookids)):
        arr.append(Library(bookids[i], books[i], authors[i], subjects[i], availablebooks[i]))    
    student = Student(arr)
    librarian = Librarian(arr)
    done = False
    while done == False:
        print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Add a Book
                  5. Delete a Book
                  6. Search a Book
                  7. Modify a Book
                  8. Exit
                  """)
        choice=int(input("Enter Choice:"))
        if choice==1:
            library.displayAvailablebooks(arr)
        elif choice==2:
            library.lendBook(student.requestBook())
        elif choice==3:
            library.addreturnBook(student.returnBook())
        elif choice==4:
            arr.append(librarian.addBook())
        elif choice==5:
            librarian.deleteBook()
        elif choice==6:
            library.searchDisplay(arr)
        elif choice==7:
            librarian.modifyBook()
        elif choice==8:
            sys.exit()

main()
