'''PROBLEM 4: Alphabetical Numbers
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:

alpha_list = [zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]

I= list integers 0-19
O= list integers ordered by alpha order

D= lists
A
define alpha_list
create helper function that transforms int value in alphabet,
    def int_to_str
        int = alpha_list[int]
        return int
original list ordered with sorted(original_list, key=int_to_str)

C
'''

alpha_str = "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"

alpha_list = alpha_str.split(',')

def int_to_str(my_int):
    alpha_int = alpha_list[my_int]
    return alpha_int

def alphabetic_number_sort(my_list):
    sorted_list = sorted(my_list, key=int_to_str)
    return sorted_list

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

##lsBot clean list from spaces and change constant to capital letters

ALPHA_STR = "zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen"

ALPHA_LIST = [s.strip() for s in ALPHA_STR.split(',')] # opt A, strip
# ALPHA_LIST = alpha_str.split(', ')] # opt B, add extra space in separator to remove from new list

def int_to_str(my_int):
    return ALPHA_LIST[my_int]

def alphabetic_number_sort(my_list):
    return sorted(my_list, key=int_to_str)

'''PROBLEM 2: Merge Sets
Given two lists, convert them to sets and return a new set which is the union of both sets.
P
I = 2 lists
O = union of both lists
E
-lists can have different length
D = lists and sets
A
transform lists to sets and perform union on both
C
'''

def merge_sets(lst1, lst2):
    return set(lst1).union(set(lst2))

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True

'''PROBLEM 3: Immutable intersection
Transform two lists into frozen sets and find their common elements.
P
I = lists
O = intersection set
E
D = lists and sets
A
transform lists to sets and return the intersection
C'''

def intersection(lst1, lst2):
    return frozenset(lst1) & frozenset(lst2))

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

'''PROBLEM 4: Arrange a Dictionary
Given a dictionary, return its keys sorted by the values associated with each key.
P
I=dict
O=sorted list of keys by values
E
D
dict and lists
A
create a list with keys sorted
C
'''

def sort_value(item):
    return item[1]

def order_by_value(my_dict):
    sorted_items = sorted(my_dict.items(), key=sort_value)
    return [key for key, value in sorted_items]

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

## using lambda (mini function)

def order_by_value(my_dict):
    return sorted(my_dict.keys(), key=lambda dict_key: my_dict[dict_key])

'''PROBLEM 5
From two list arguments, determine the elements that are unique to the first list. The return value should be a set.
P I = 2 lists O = set difference
RULES E from the examples is clear that the return should be the difference of the sets
D lists and sets
A transform lists into sets
perform difference operation and return result
C'''

def unique_from_first(lst1, lst2):
    return set(lst1).difference(set(lst2))

# All of these examples should print True
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

'''PROBLEM 6: Leading substrings
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest
P
I = string
O = list of substrings
rules
-each subs starts with the first letter
-list shoudl be ordered from shortest to longest
E
D
strings, substirngs, and list
A
create new list
loop through list while starting from index[0]
    count = 1
    create subst with slice from original string ->[0:1]
        add subst to list
    stop loop when count > len(str)

will try to do it directly with a lit comprehension
C
'''
def leading_substrings(my_str):
    return [my_str[0:(idx+1)] for idx in range(len(my_str))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

## lsBot -> when you start a slice from the beginning omit the 0

def leading_substrings(my_str):
    return [my_str[:idx + 1] for idx in range(len(my_str))]

'''PROBLEM 7: All substrings
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:
P
I=string
O=substring
RULES
-Order the returned list by substring begins
-all substrings starting at index position 0 -> first
-the multiple substrings of each position should be order shortest to longest
E
D
string with indeces, substrings, and list
A
create empty list -> subst_list
iterate through each char slicing the original string
    with the new string -> apply function leading_substrings
    add the list to the subst_list
return subst_list
C
'''
def leading_substrings(my_str):
    return [my_str[:idx + 1] for idx in range(len(my_str))]

def substrings(my_str):
    list_str = [my_str[idx:] for idx in range(len(my_str))]
    final_list =[]
    for word in list_str:
        final_list.extend(leading_substrings(word))
    return final_list

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

## lsBot suggestion to simplify my solution and loop directly with the words

def leading_substrings(my_str):
    return [my_str[:idx + 1] for idx in range(len(my_str))]

def substrings(my_str):
    final_list =[]
    for idx in range(len(my_str)):
        sub_word = my_str[idx:]
        final_list.extend(leading_substrings(sub_word))
    return final_list

##  LS solution, nested list comprehension
    # 1. outer loop for string possibilities based on index
    # 2. inner loop for all substrings possibilities of each string using leading_substrings function from previous exercise

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]

'''PROBLEM 8: Palindromic substrings
Write a function that returns a list of all palindromic substrings of a string. That is, each substring must consist of a sequence of characters that reads the same forward and backward. The substrings in the returned list should be sorted by their order of appearance in the input string. Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.
P
I = string
O = list of palindromic substrings
RULES
-palindrome is strings read the same forward and backward
-substring list should be ordered by appearance
-duplicate substrings should appear twice
E
-from examples strings separated by '-' count as one
D
string and lists
A
helper function to extract all posible words from main string
2nd helper function to extract all substrings from each word
3rd function -> palindromes to extract all the palindromes from the substring list
C
'''

def leading_substrings(my_str):
    return [my_str[idx:] for idx in range(len(my_str))]

def substrings(my_str):
    substr_list = []
    for word in leading_substrings(my_str):
        substr_list.extend([word[:idx + 1] for idx in range(len(word))])
    return substr_list

def palindromes(my_str):
    palindrome_list = []

    for substring in substrings(my_str):
        if substring == substring[::-1] and len(substring) > 1:
            palindrome_list.append(substring)

    return palindrome_list

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

## simplify last part of the code with list comprehension and another help function

def is_palindrome(substring):
    return substring == substring[::-1] and len(substring) > 1

def palindromes(my_str):
    return [substring for substring in substrings(my_str) if is_palindrome(substring)]

'''PROBLEM 9: Inventory Item Transactions
Write a function that takes two arguments, an inventory item ID and a list of transactions, and returns a list containing only the transactions for the specified inventory item.
P
I = id(value) and list of dict
O = returns list of dict with that value
R

E
D
list, dictionaries
A
for dict in list
    if key:value == id(value)
    append dict to list

we can do this with a list comprehension
C
'''

def transactions_for(item_id, my_list_transactions):
    return [my_dict_transaction for my_dict_transaction in my_list_transactions if my_dict_transaction['id'] == item_id]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

'''PROBLEM 9: Inventory Item Availability
Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.
P
I = item_id, list of dictionaries (transactions)
O = True or False - if item is available or not
R
-true -> if summary of all quantities is > 0
-in will add and out will substract
E
D
list of dictionary, key[values]
A
filter dictionaries with function from prev exercise
for transaction in transactions:
    count = 0
    if transaction[movement] == 'in':
        count += transaction['quantity']
    else:
        count -= transaction['quantity']

return count > 0
C
You may (and should) use the transactions_for function from the previous exercise.
'''

def transactions_for(item_id, my_list_transactions):
    return [my_dict_transaction for my_dict_transaction in my_list_transactions if my_dict_transaction['id'] == item_id]

def is_item_available(item_id, transactions):
    relevant_transactions = transactions_for(item_id, transactions)
    count = 0

    for transaction in relevant_transactions:
        if transaction['movement'] == 'in':
            count += transaction['quantity']
        else:
            count -= transaction['quantity']

    return count > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True