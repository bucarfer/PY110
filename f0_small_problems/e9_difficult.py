### PROBLEM 1 TRANSPOSE 3 X 3
# Write a function that takes a list of lists that represents a 3x3 matrix and returns the transpose of the matrix. You should implement the function on your own, without using any external libraries.
# Take care not to modify the original matrix -- your function must produce a new matrix and leave the input matrix list unchanged.

'''P
I = list of lists (matrix)
O = list of lists (matrix) -> transpose
E
D using zip to create a zip object and transform it into a list, input cannot be mutated
Idea
flatten list and then create new lists getting every 3 items (option B, not used)

using zip to create new objects with the first of each list and then converting this into a list
A
- unpack matrix into 3 different lists
- use zip with the 3 lists and convert to list of tuples
- use a list comprehension to transform tuples to lists
- return new lists
C'''

def transpose(matrix):
    list1, list2, list3 = matrix
    transpose_tuple = list(zip(list1, list2, list3))

    return [list(my_tuple) for my_tuple in transpose_tuple]


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

## lsBot suggestions:
# - unpack directly with *
# - transpose_tuple renamed to transpose_columns
# - rename tuple to my_tuple

def transpose(matrix):
    return [list(my_tuple) for my_tuple in list(zip(*matrix))]

### PROBLEM 2 TRANSPOSE MxN Matrix

# Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

# same solution works:
def transpose(matrix):
    transpose_tuple = list(zip(*matrix))

    return [list(my_tuple) for my_tuple in transpose_tuple]

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]]) # 1 line 4 units -> 4 columns 1 item
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]]) # 4 lines 1 unit -> 4 columns 1 item
print(transpose([[1]]) == [[1]]) # 1 line 1 unit

matrix_3_by_5 = [
    [1, 2, 3, 4, 5], # 3 lists 5 units -> 5 lists 3 items
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

## try LS approach using nested loops
'''
Idea
create new matrix with as many columns (lists) as items in the first list
    [[] for item in range(len(matrix[0]))]
E
index[0] of each list -> add to new matrix[0]
...
index[4] of each list -> add to new matrix[4]
A
for lines in matrix:
    for index in range(len(line)):
        new_matrix[index].append(line[index])
'''

def transpose(matrix):
    new_matrix = [[] for _ in range(len(matrix[0]))]

    for row in matrix:
        for column_idx in range(len(row)):
            new_matrix[column_idx].append(row[column_idx])

    return new_matrix

## if we have matrix with rows of different lengths we could solve it with:

def transpose_ragged(matrix, fillvalue=None):
    new_cols = max(len(row) for row in matrix)
    new_matrix = [[] for _ in range(new_cols)]

    for row in matrix:
        for col_idx in range(new_cols):
            value = row[col_idx] if col_idx < len(row) else fillvalue
            new_matrix[col_idx].append(value)
    return new_matrix

matrix_3_by_5 = [
    [1, 2, 3],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [None, 1, 6],
    [None, 0, 2],
]

print(transpose_ragged(matrix_3_by_5) == expected_result)

### PROBLEM 3: ROTATING MXN MATRICES
# Write a function that takes an arbitrary MxN matrix, rotates it clockwise by 90-degrees as described above, and returns the result as a new matrix. The function should not mutate the original matrix.

'''P
I = matrix of lists (M x N)
O = matrix of lists rotate (N x M)
E and A
- n of lists new_matrix = len(matrix[0])
- [3, 7, 4, 2],
  [5, 1, 0, 8],

  result 4 lists
  [5, 3] line[0] of matrix[1] and matrix[0]


for idx_line in range(len(matrix[0]) # [0, 1, 2, 3]
    for idx in range(len(matrix), -1, -1) # [1, 0]
        new_matrix[idx_line].append(matrix[idx][idx_line]) # new_matrix[0].append(matrix[1][0])
D
list of lists for input and output
A
- create a result list wih columns empty lists (the new rows)
- for each column index c from 0 to -1
    - for each row index r from -1 down to 0
        - append matrix[r][c] to result[c]
C'''

def rotate90(matrix):
    new_matrix = [[] for _ in range(len(matrix[0]))]

    for idx_column in range(len(matrix[0])):
        for idx_row in range(len(matrix) - 1, -1, -1):
            new_matrix[idx_column].append(matrix[idx_row][idx_column])

    return new_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

# LS alternative using slicing and unpacking

def rotate90(matrix):
    # Reverse the rows, then transpose
    return [list(row) for row in zip(*matrix[::-1])]

### PROBLEM 4: MERGED SORTED LISTS

# Write a function that takes two sorted lists as arguments and returns a new list that contains all the elements from both input lists in ascending sorted order. You may assume that the lists contain either all integer values or all string values.

# You may not provide any solution that requires you to sort the result list. You must build the result list one element at a time in the proper order.

# Your solution should not mutate the input lists.

'''P
I = 2 sorted lists
O = merged list in ascending order
R
- lists contain either all num or all strings
- do not use sort in result list
- build the result list one by one in proper order
- solution should NOT mutate original lists
E
- if one empty list will -> solution other list
- both lists can have different lenghts
D
lists
A
idea
iterate a copy of both lists and compare item by item, smaller one gets added to the new list and remove from copy list

- create copy of both lists
- create new_list = []

- while len(lists) are different to 0:
        if list1[0] smaller than list2[0]:
            append list1[0] to the new list and remove from copy
        else:
            append list12[0] to the new list and remove from copy

- return new_list
C'''

def merge(list1_original, list2_original):
    new_list = []
    list1 = list1_original.copy()
    list2 = list2_original.copy()

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1[0])
            list1.pop(0)
        else:
            new_list.append(list2[0])
            list2.pop(0)

    while len(list1) != 0:
        new_list.append(list1[0])
        list1.pop(0)

    while len(list2) != 0:
        new_list.append(list2[0])
        list2.pop(0)

    return new_list

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

## LSbot suggestions, simplified code by concatenating the remaining elements of the copied lists instead of keep mutating them

def merge(list1_original, list2_original):
    new_list = []
    list1 = list1_original.copy()
    list2 = list2_original.copy()

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))

    return new_list + list1 + list2

## Alternative solution, using indexes

def merge_2(list1, list2):
    i = j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # last index leftover from the comparison
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

## PROBLEM 5: MERGE SHORT

# Write a function that takes a list argument and returns a new list that contains the values from the input list in sorted order. The function should sort the list using the merge sort algorithm as described above. You may assume that every element of the list will have the same data type: either all numbers or all strings.

'''
P Implement merge sort: returning new list with input list in ascending order
I= list of elements (same data type)
O= sorted list of elements (ascending order)
R
-list should be sorted with sort algorithm
    - split into single elements sublists
-repeat merge sublists until only one sorted list remains
-do not mutate original list
-all elements are same type - either num or strings
E
examples behave as expected
D
lists and sublists
A
- split the list into single elements sublists with a list comprehension
- use a while loop -> while len(sublists)>1
    merge function with every 2 sublists until the result is one single list
        if there is an odd leftover sublist, append it as-is to 'merged'
- return sublist[0]
C'''

# Feel free to use the merge function you wrote in the previous exercise.

def merge(list1_original, list2_original):
    new_list = []
    list1 = list1_original.copy()
    list2 = list2_original.copy()

    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            new_list.append(list1.pop(0))
        else:
            new_list.append(list2.pop(0))

    return new_list + list1 + list2

def merge_sort(my_list):
    sublists_list = [[item] for item in my_list]

    while len(sublists_list) != 1:
        if len(sublists_list) % 2 == 0:
            sublists_list = [merge(sublists_list[idx], sublists_list[idx + 1]) for idx in range(len(sublists_list)) if idx % 2 == 0]
        else:
            sublists_list = [merge(sublists_list[idx], sublists_list[idx + 1]) for idx in range(len(sublists_list) - 1) if idx % 2 == 0] + sublists_list[-1:]

    return sublists_list[0]

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7]) #5 - 0, 1, 2, 3, 4
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)

## LSbot improvements
# return an empty list if not list
# simplified the odd and even options with a unique range sequence than pairs sublists and add any remaining even leftover at the end
# merge function -> use indexes instead of popping elements from the list

def merge(list1, list2):
    new_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    return new_list + list1[i:] + list2[j:]

def merge_sort(my_list):
    if not my_list:
        return []

    sublists = [[item] for item in my_list]

    while len(sublists) > 1:
        merged = [merge(sublists[idx], sublists[idx + 1]) for idx in range(0, len(sublists) - 1, 2)]
        if len(sublists) % 2 == 1:
            merged += sublists[-1:]

        sublists = merged

    return sublists[0]

#LS solution: recursive merge sort
# function calls itself multiple times, I understand the function, but it is hard to use it by myself

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    sub_list1 = lst[:len(lst) // 2]
    sub_list2 = lst[len(lst) // 2:]

    sub_list1 = merge_sort(sub_list1)
    sub_list2 = merge_sort(sub_list2)

    return merge(sub_list1, sub_list2)

### PROBLEM 6: BINARY SEARCH

#Implement a binary_search function that takes a list and a search item as arguments, and returns the index of the search item if found, or -1 otherwise. You may assume that the list argument will always be sorted.

'''
P = Implement binary search in a function and return index , -1 if not found
I = 2 arguments -> list and search item
O = integer (index of search or -1 if not found)
R
- list will be always sorted (ascending)
- lists can be strings or integers (always comparable)
- if item is not found it will return -1
    -> use search element in [list] -> return True or False
E
D
lists
A
-retrieve middle value -> list[len(list)//2]
    if is equal to search item
        return search item
    if is less than search item
        discard the first half including the item
    if is more than search item
        discard second half including item

- keep process until you find the value
- if not item found
    return -1
C'''

def binary_search(my_lst, i):
    lst = my_lst.copy()

    while len(lst) > 1:
        if lst[len(lst)//2] == i:
            return my_lst.index(i)
        elif lst[len(lst)//2] < i:
            lst = lst[len(lst)//2 + 1:]
        elif lst[len(lst)//2] > i:
            lst = lst[:len(lst)//2]

    if len(lst) == 1 and lst[0] == i:
        return my_lst.index(i)

    return -1


# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)

# print(binary_search(businesses, 'Apple Store') == 0)

# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
# print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

# names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
#          'Tyler']
# print(binary_search(names, 'Peter') == -1)
# print(binary_search(names, 'Tyler') == 6)

# new algorithm with LSbot tips

'''
A
- init low = 0 and high = len(lst) # - 1

- keep while loop if low is less or equal to high
    - init middle = (low + high) // 2
    if list[middle] == s_item
        return middle
    elif list[middle] < s_item  # [1, 2, 3, 4, 5]
        low = middle + 1
    else:
        high = middle - 1

- if loop ends return -1
'''

def binary_search(lst, s_item):
    low = 0
    high = len(lst) - 1 # -1 is to avoid the index to get out of range where the search item is greater than the list

    while low <= high:
        middle = (low + high) // 2
        if lst[middle] == s_item:
            return middle
        elif lst[middle] < s_item:
            low = middle + 1
        else:
            high = middle - 1

    return -1

### PROBLEM 7: EGYPTIANS FRACTIONS

# unit fraction -> rational number where numerator is 1

# egyptian number is summary of series of unit fractions

# Write two functions: one that takes a Rational number as an argument, and returns a list of the denominators that are part of an Egyptian Fraction representation of the number, and another that takes a list of numbers in the same format, and calculates the resulting Rational number. You will need to use the Fraction class provided by the fractions module.

'''
1st function
P = takes rational number (numerator/denominator) and returns the denominators of its egyptian number
I = rational number (numerator/denominator)
O = integers (denominators of egyptian number)
R & E
from examples
- fractions are all positive numbers
- from example
    1   1   1   1
2 = - + - + - + -
    1   2   3   6

1/ 1 = 1 1 / 2 = 0.5 1 / 3 = 0.3 1 / 6 = 0.17
-why does it skip the denominators 4 and 5 because the result will be greater than the rational number!
D
fractions and list
A
init denominator = 1
init list_denominator = []
- while True:
    inside the while True init:
    current_sum = sum(Fraction(1, denom) for denom in list_denominator)
    possible_denominator = Fraction (1/denominator)
    remaining = my_fraction - current_sum

    if remaining == 0:
            return list_denominator
        if possible_denominator <= remaining:
            list_denominator.append(denominator)
        denominator += 1
C'''

from fractions import Fraction

def egyptian(my_fraction):
    denominator = 1
    list_denominator = []

    while True:
        current_sum = sum(Fraction(1, denom) for denom in list_denominator)
        possible_denominator = Fraction(1, denominator)
        remaining = my_fraction - current_sum

        if remaining == 0:
            return list_denominator
        if possible_denominator <= remaining:
            list_denominator.append(denominator)
        denominator += 1

'''
2nd function
P = transform egyptian number back to fraction number
I = list of integers (denominators)
O = 2 integers (numerator and denominator)
R
E
D
fractions and lists
A
- create a list comprehension with all rational numbers and return summary of them
C'''

def unegyptian(my_denominators):
    return sum([Fraction(1, denominator) for denominator in my_denominators])

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))

## lsBot corrections:

# Inputs aren’t limited to values greater than 1. The exercise includes numbers less than 1 as well (e.g., 1/2). Your code already handles that, which is great.
# In egyptian, recomputing current_sum each loop makes the code busier than it needs to be. It’s simpler to keep a running remainder and update it when you accept a unit fraction.
# Prefer a clear loop condition over while True when you have a natural stop condition.
# Naming: list_denominator → denominators, my_fraction → target, possible_denominator (which is actually a unit fraction) → unit or candidate_unit. That makes intent clearer.
# Good job using Fraction(1, denominator) instead of Fraction(1/denominator). Passing a float to Fraction can produce unexpected results.
# Here’s a cleaned-up version of your first function with the same logic:

from fractions import Fraction

def egyptian(my_fraction):
    list_denominator = []
    denominator = 1
    remaining = my_fraction

    while remaining != 0:
        unit = Fraction(1, denominator)
        if unit <= remaining:
            list_denominator.append(denominator)
            remaining -= unit
        denominator += 1

    return list_denominator

def unegyptian(denoms):
    return sum([Fraction(1, d) for d in denoms])