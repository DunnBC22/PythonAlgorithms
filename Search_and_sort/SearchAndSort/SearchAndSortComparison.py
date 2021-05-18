'''
help from the following:
    https://wiki.c2.com/?QuickSortInPython
    https://runestone.academy/runestone/books/published/pythonds/index.html
'''

from Sort import Sort
from Search import Search
import datetime

# Read in random Numbers from a text file
random_numbers = []
with open('Random Numbers.txt', 'r') as file:
    for line in file:
        line = int(line.strip())
        random_numbers.append(line)

# Remove duplicates
brn = datetime.datetime.now()
random_num = Search.remove_all_duplicates(random_numbers)
arn = datetime.datetime.now()
print('\nThe duration of the removing duplicates method is', arn-brn)
print("The list of", len(random_numbers), 'items was reduced to',
      len(random_num), 'after removing duplicates.')

# The Sorting algorithms
print('\nAnd now for the Sorting algorithms...')

before_ss = datetime.datetime.now()
merge_sort = Sort.shell_sort(random_num)
after_ss = datetime.datetime.now()
print('The duration of the shell sort is', after_ss-before_ss)

b_m_s = datetime.datetime.now()
merge_sort = Sort.merge_sort(random_num)
a_m_s = datetime.datetime.now()
print('The duration of the merge sort is', a_m_s-b_m_s)

e = datetime.datetime.now()
bubble_sort = Sort.bubble_sort(random_num)
f = datetime.datetime.now()
print('The duration of the bubble sort is', f-e)

g = datetime.datetime.now()
selection_sort = Sort.selection_sort(random_num)
h = datetime.datetime.now()
print('The duration of the selection sort is', h-g)

x = datetime.datetime.now()
insertion_sort = Sort.insertion_sort(random_num)
y = datetime.datetime.now()
print('The duration of the insertion sort is', y-x)

b4_quick_sort = datetime.datetime.now()
#quick_sort = Sort.quick_sort(random_num, 0, len(random_num)-1)
quick_sort = Sort.quick_sort(random_num)
after_quick_sort = datetime.datetime.now()
print('The duration of the quick sort is', after_quick_sort-b4_quick_sort)

# The searching algorithms
print('\nAnd now for the Search algorithms...')
value = 769830
bef_seq = datetime.datetime.now()
sequential_search = Search.seq_search(insertion_sort, value)
after_seq = datetime.datetime.now()
print("The duration of the sequential search is ", after_seq-bef_seq)

b_bin = datetime.datetime.now()
binary_search = Search.binary_search(insertion_sort, value)
a_bin = datetime.datetime.now()
print("The duration of the binary search is ", a_bin-b_bin)
