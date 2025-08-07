'''problem 1
Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending_list = sorted(lst)
descending_list = sorted(lst, reverse=True)

print(ascending_list)
print(descending_list)

# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

'''problem 2
Repeat the previous exercise but, this time, perform the sort by mutating the original list.'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# ascending
lst.sort()
print(lst)

#descending
lst.sort(reverse=True)
print(lst)

'''problem 3
Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.
'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

lst.sort(key=str)
print(lst)

lst.sort(key=str, reverse=True)
print(lst)

'''problem 4
How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?
'''

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def year_published(my_dict):
    return int(my_dict['published'])

sorted_books = sorted(books, key=year_published)
print(sorted_books)