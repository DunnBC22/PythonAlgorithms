from MovieQueue import Queue

Movies = Queue()

print("Size of movie queue:", Movies.size())
print("Is the movie queue empty?", Movies.isEmpty())

MovieNames = ['Knives Out', 'Return of the Jedi', 'Joker', 'Batman', 'The Dark Knight', 'Airplane!', 'Up', 'Amedeus',
              'Ghostbusters', 'Oceans 11', 'The Lion King', 'West Side Story', 'Fight Club', 'Ferris Bueller\'s Day off', 'Back to the Future']

for x in range(len(MovieNames)):
    Movies.enqueue(MovieNames[x])


print("Size of movie queue:", Movies.size())
print("Dequeued item:", Movies.dequeue())
print(Movies.size(),  '\n')
Movies.showAllItems()
