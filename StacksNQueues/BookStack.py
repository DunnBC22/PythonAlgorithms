from Book import Book
# use a list as a Stack


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if (self.size() > 0):
            return self.items[len(self.items)-1]
        elif (len(self.items) == 0):
            return "Cannot see the next item because there are no items in this stack."

    def showAllItems(self):
        for x in range(len(self.items)):
            print(self.items[x])

    def bulkImport(self):
        bookList = []
        with open('books.txt', 'r') as file:
            for line in file:
                anotherBook = 0
                self.title, self.author, self.genre = line.split(',')
                anotherBook = Book(self.title)
                print(anotherBook.getTitle())
                anotherBook.setAuthor(self.author)
                print(anotherBook.getAuthor())
                anotherBook.setGenre(self.genre)
                print(anotherBook.getGenre())
                bookList.append(anotherBook)
            return bookList

    # this method is not working
    def showImportedBooks(self):
        for x in range(len(self.items)):
            print(x)
            print('Title:', self.items[x].getTitle(), ', Author:', self.items[x].getAuthor(
            ), ', and Genre:', self.items[x].getGenre())
