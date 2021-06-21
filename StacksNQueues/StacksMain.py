from BookStack import Stack
from Book import Book

# Part 1
newBook = Book('Bob the Builder is Building')
newBook.setAuthor('Tim Nobody')
newBook.setGenre('Comedy')
print('Info for the single book stack:')
print(newBook.title)
print(newBook.getAuthor())
print(newBook.getGenre())

# Part 2
learningTechBooks = Stack()
print("\nLength of a new stack of books before adding books:",
      learningTechBooks.size())

booksList = ['Catcher in the Rye', 'The Great Gatsby',
             'To kill a Mockingbird', '1984', 'Into Thin Air']

for x in range(len(booksList)):
    learningTechBooks.push(booksList[x])

print("\nStack length after adding a few books:", learningTechBooks.size())
learningTechBooks.showAllItems()
learningTechBooks.pop()
print("\nStack length after pop method:", learningTechBooks.size(), '\n')
learningTechBooks.showAllItems()
print('\nwhat is the next book on the top of the stack?\n')

print(learningTechBooks.peek(), '\n')
