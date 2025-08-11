'''PROBLEM 1
Consider the following nested dictionary:

Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

A
def age_male = 0
loop through outer dictionary
access inner dictionary and the value of the age keys
    if gender = male
    add to age_male variable
return age variable
'''

## solution with traditional loop

age_male = 0

for info in monsters_dict.values():
    if info['gender'] == 'male':
            age_male += info['age']

print(age_male)

monsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

## solution with comprehension

print(sum([info['age'] for info in monsters.values() if info['gender'] == 'male']))

'''PROBLEM 2
Given the following data structure, return a new list with the same structure, but with the values in ea
ch sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)
The string values should be sorted as strings, while the numeric values should be sorted as numbers.

A
new list
iterate through list
    for item in sublist
        if item.isalpha():
        sorted_list = sorted(sublist)
        append sorted_list to new_list
        if item.isdigit():
        sorted_num = sorted(sublist, key=int)
        append sorted_num to new_list
return new_list
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# expected result
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

for sublist in lst:
    if isinstance(sublist[0], str):
        sublist.sort()
    else:
        sublist.sort(key=int)

print(lst)

## using comprehensions (new list)
print([sorted(sublist) if isinstance(sublist[0], str) else sorted(sublist, key=int) for sublist in lst])

## lsBor, sorted knows how to differentiate between strings and integers

print([sorted(sublist) for sublist in lst])

'''PROBLEM 3:
Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings (that is, the numbers should be treated as strings). Use a comprehension if you can. (Try using a for loop first.)
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

#expected result first
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

print([sorted(sublist, key=str) for sublist in lst])

'''PROBLEM 4:
Given the following data structure, write some code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second.
'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }

print({sublist[0]: sublist[1] for sublist in lst})

'''PROBLEM 5:
Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.
A
first we create a function that sums up the odd numbers od the sublist

then we sort the list using this function as the key

'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]] ## expected result

def sum_odd(my_list):
    return sum([ num for num in my_list if num % 2 == 1])

print(sorted(lst, key=sum_odd))

'''PROBLEM 6:
Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

A
we first create a dictionary where each value is incremented by one
then we return this new dictionaries to the list dict loop
'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}] EXPECTED

print([{key: value + 1 for key, value in my_dict.items()} for my_dict in lst])

'''PROBLEM 7:
Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.
A
1. first we create a list only with multiples of 3
2. we transform the original list with a transformation comprehension
'''
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
# [[], [3, 12], [9], [15, 18]] expected

print([[item for item in sublist if item % 3 == 0] for sublist in lst])

'''PROBLEM 8:
Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

'''

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

new_list = []
for info in dict1.values():
    if info['type'] == 'fruit':
        new_list.append([color.capitalize() for color in info['colors']])
    if info['type'] == 'vegetable':
        new_list.append(info['size'].upper())

print(new_list)

# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"] #expected return

## LS do it creating a function helper

def transform_item(info):
    if info['type'] == 'fruit':
        return [color.capitalize() for color in info['colors']]
    else:
        return info['size'].upper()

print([transform_item(info) for info in dict1.values()])

'''PROBLEM 9:
This problem may prove challenging. Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return a list that contains only the dictionaries where all the numbers are even.

I= list
O= list with only dict with all even numbers

A
iterate through dict in list
check all the values (inner lists) of all pairs are even % 2 == 0:
    only when even return dict
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

[{'e': [8], 'f': [6, 10]}]

def even_dict(my_dict):
    for my_list in my_dict.values():
        for item in my_list:
            if item % 2 != 0:
                return False
    return True

print([my_dict for my_dict in lst if even_dict(my_dict)])

## LS using all function

def even_dict(my_dict):
    for my_list in my_dict.values():
        if not (all([item % 2 == 0 for item in my_list])):
            return False

    return True

print([my_dict for my_dict in lst if even_dict(my_dict)])

'''PROBLEM 10
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, even when some of those items were created on a different server or by a different application. That is, without any synchronization, two or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each other's toes. It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed. There are several UUID versions, each with some non-random characteristics in some of the bits. These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.

I=nothing
O=string -> pattern 8-4-4-4-12

rules
digits 0-9 and letters a-f

A
create random choice from digits and letters
and add them to string with 8, 4, 4, 4, and 12.
each string is a list element, join them with "-" to form a unique string
'''
## 1st attempt

import random

def uuids():
    char_opt = '0123456789abcdef'

    my_char1 = random.choices(char_opt, k=8)
    my_char2 = random.choices(char_opt, k=4)
    my_char3 = random.choices(char_opt, k=4)
    my_char4 = random.choices(char_opt, k=4)
    my_char5 = random.choices(char_opt, k=12)

    my_list = [my_char1, my_char2, my_char3, my_char4, my_char5]

    final_list = [''.join(sublist) for sublist in my_list]

    return "-".join(final_list)

## 2nd attempt using list comprehensions

import random

def uuids():
    char_opt = '0123456789abcdef'
    patterns = [8, 4, 4, 4, 12]
    uuid = []

    for pattern in patterns:
        chars = random.choices(char_opt, k=pattern)
        uuid.append(''.join(chars))

    return "-".join(uuid)

## lsBot using random.choice instead of random.choices

import random

def generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

## further simplify the day after
import random

def uuid_creator():
    options = '0123456789abcdef'
    pattern = [8, 4, 4, 4, 12]


    uuid_list = [''.join(random.choices(options, k=item)) for item in pattern]
    return '-'.join(uuid_list)

print(uuid_creator())

'''PROBLEM 11
The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.
O=list with lists as values
I=list
A
iterate through the dict values
    iterate through items of each list
        if char == vowel
        append(char)
'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowel = 'aeiou'

list_of_vowels= [char for my_list in dict1.values() for item in my_list for char in item if char in vowel]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']