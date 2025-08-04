'''
EXERCISE 1 Cute Angles:
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

P
I = floating point number representing angle 0-360
O = string rep angle in degrees, minutes, and sec

RULES
- degree symbol (°), minutes ('), and seconds (")
- 60 minutes in a degree, and 60 seconds in a minute.

E
- from examples floating number can have up to 6 decimals
- some of the angles have 2 solutions

D
floating numbers, list, and strings

A
def function
create empty list
get int numbers and append to list (transform to str and add syb)
decimals degrees to be multiply by 60 to transform into minutes
    get integers and append to list (transform to str and add syb)
decimals minutes to be multiply by 60 to transform into seconds
    get integers and append to list (transform to str and add syb)
return list with join method ''

C
'''

def get_next_unit(result):
    result = result - int(result)
    result = result * 60
    return result

def dms(num):
    my_list = []

    my_list.append(f'{(int(num))}°')
    num = get_next_unit(num)
    my_list.append(f"{(int(num)):02}'")
    num = get_next_unit(num)
    my_list.append(f'{(int(num)):02}"')

    return ''.join(my_list)

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

## use constants (with my example not very useful, but done)

DEGREE = "\u00B0"  # degree symbol
MINUTES_PER_DEGREE_OR_SECONDS_PER_MINUTE = 60

def get_next_unit(result):
    result = result - int(result)
    result = result * MINUTES_PER_DEGREE_OR_SECONDS_PER_MINUTE

    return result

def dms(num):
    my_list = []

    my_list.append(f'{(int(num))}{DEGREE}')
    num = get_next_unit(num)
    my_list.append(f"{(int(num)):02}'")
    num = get_next_unit(num)
    my_list.append(f'{(int(num)):02}"')

    return ''.join(my_list)

'''
EXERCISE 2: Combining lists

Write a function that takes two lists as arguments and returns a set that contains the union of the values from the two lists. You may assume that both arguments will always be lists.

P
I = 2 lists
O = set with union of the values from both lists

RULES
imput will be always to lists
return union set of both

E

D
lists and sets

A

transfor both lists into sets
combine them with union method

C
'''

def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    new_set = set1.union(set2)

    return new_set


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

## lsBot step, combining steps

def union(list1, list2):
    return set(list1).union(set(list2))


'''EXERCISE 3 Halvsies:
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

P
I list as an argument
O list that contains two elements, both of which are lists

R
-first half of the original list elements in the first element
-put the second half in the second element
    -if odd number of elements, place the middle element in the first half
E
-shows how a list of one element behaves (still 2 lists output)
-shows how an empty list behaves (still 2 lists output)
D
lists
A
len of list
    if list % 2 == 1
        list1 = list first half + 1 with slice
        list2 = list second half with slice
    else:
        list1 = list first half with slice
        list2 = list second half with slice

create list with 2 empty lists
list[0] = list1
list[1] = list2

return new_list

C
'''

def halvsies(my_list):
    l = len(my_list) // 2 #hola 4 -> 2
    if len(my_list) % 2 == 1:
        list1 = my_list[:(l + 1)]
        list2 = my_list[(l + 1):]
    else:
        list1 = my_list[:l]
        list2 = my_list[l:]

    new_list = []
    new_list.append(list1)
    new_list.append(list2)

    return new_list


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

##
# 1. simplifies if/else with math trick that covers all cases for odd and even
# 2. return both lists directly

def halvsies(my_list):
    mid_point = (len(my_list) + 1) // 2

    list1 = my_list[:mid_point]
    list2 = my_list[mid_point:]

    return [list1, list2]

'''EXERCISE 4 Find the duplicate:

Given an unordered list and the information that exactly one value in the list occurs twice (every other value occurs exactly once), determine which value occurs twice. Write a function that finds and returns the duplicate value.

P
I = unorderd list with one duplicate element
O = return duplicate value

RULES

E
-based on the example no limit of elements
-what happens if more than one element is duplicated?
    We assume only one

D
list

A
1. iterate through list
2. if count of item is == 2
    return item

C
'''

def find_dup(my_list):
    for item in my_list:
        if my_list.count(item) == 2:
                return item

print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True

## LsBot, incomplete answer -> use sets instead

def find_dup(my_list):
    rep_set = set()

    for item in my_list:
        if item in rep_set:
            return item
        else:
            rep_set.add(item)

## correction -> the if block has a return statement, the function will immediately exit if that condition is met.

def find_dup(my_list):
    rep_set = set()

    for item in my_list:
        if item in rep_set:
            return item
        rep_set.add(item)

## alternative using list comprehensions:

def find_dup(my_list):
    dup = [item for item in my_list if my_list.count(item) == 2]
    return dup[0]

'''EXERCISE 5: Combine two lists:

Write a function that combines two lists passed as arguments and returns a new list that contains all elements from both lists arguments, with each element taken in alteration.
You may assume that both input lists are non-empty, and that they have the same number of elements.
P
I 2 lists as arguments
O 1 combined list with elements altered

rules
both list have same number of elements and non-empty
E
example shows elements are altered, one from each list
D
lists
A
create empty list
combine both lists with zip and assigned to new list variable
loop over tuples of list, transform tuples to lists, and concatenate lists
return list
C
'''

def interleave(list1, list2):
    total = []
    comb_list = list(zip(list1, list2))
    for item in comb_list:
        total += item
    return total

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

## LS solution

def interleave(list1, list2):
    total = []

    for idx in range(len(list1)):
        total.extend([list1[idx], list2[idx]])

    return total

## LSbot suggestion to use list comprehension:



def interleave(list1, list2):
    return [element for pair in zip(list1, list2) for element in pair]

'''EXERCISE 6: Multiplicative Average
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

P
I = list of positive integers
O = string with value rounded to 3 decimals

RULES
1. multiplies all of the integers together
2. divides the result by len list
3. returns result as string rounded to 3 decimals
E
D
integers and strings
A
def variable total = 1
for loop on list elements
    multiply element by total
divide total between len(list)
return f"{final:.3f}
C
'''
def multiplicative_average(my_list):
    total = 1
    for item in my_list:
        total *= item
    final = total / len(my_list)
    return f"{final:.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

## use product from math module

import math

def multiplicative_average(my_list):
    product = math.prod(my_list)
    total = product / len(my_list)
    return f"{total:.3f}"

'''EXERCISE 7: Multiply lists

Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

P
I = two list arguments (containing numbers)
O = new list -> product of each pair with same index
RULES
same number of elements
E
based on the example the numbers are integers
D
lists and integers
A
- create an empty list
- for loop of list1 len
    for each index -> new_list = list1 * list 2
-return new list
C
'''

def multiply_list(list1, list2):
    mult_list = []
    for idx in range(len(list1)):
        mult_list.append(list1[idx] * list2[idx])
    return mult_list

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

## lsBot -> use list comprehensions

def multiply_list(list1, list2):
    return [a * b for a,b in zip(list1, list2)]

'''EXERCISE 8: List of digits
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

P
I = positive integer
O = list of digits in the number
RULES
only numbers allowed
E
D
number and list
A
create empty list -> list_digit
transform number to string
for loop on string
    transform str into int and append to list_digit
return list_digit
C
'''

def digit_list(num):
    dig_list = []
    for char in str(num):
        dig_list.append(int(char))
    return dig_list

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

## lsBot _> use list comprehensions

def digit_list(num):
    return [int(char) for char in str(num)]

'''EXERCISE 9: How many?
Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").
P
I = list of elements
O = print each number with n occurrences
RULES
- case sensitive
E
D
lists and string interpolation
A
create a set from list
for loop of set
    define variable count -> item() -> method count in list
    print(item -> count)
C
'''

def count_occurrences(my_list):
    my_set = set(my_list)
    for item in my_set:
        count = my_list.count(item)
        print(f"{item} => {count}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

# # your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

## lsBot use dictionaries instead of sets

def count_occurrences(my_list):
    my_dict = {}

    for item in my_list:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1

    for key, value in my_dict.items():
        print(f"{key} => {value}")

## ls solution with method .get

def count_occurrences(my_list):
    my_dict = {}

    for item in my_list:
        my_dict[item] = my_dict.get(item, 0) + 1

    for key, value in my_dict.items():
        print(f"{key} => {value}")

## separate in 2 functions:

def print_occurrences(my_dict):
    for key, value in my_dict.items():
        print(f"{key} => {value}")

def count_occurrences(my_list):
    my_dict = {}

    for item in my_list:
        my_dict[item] = my_dict.get(item, 0) + 1

    print_occurrences(my_dict)

'''PROBLEM 10: List Average
Write a function that takes one argument, a list of integers, and returns the average of all the integers in the list, rounded down to the integer component of the average. The list will never be empty, and the numbers will always be positive integers.
P
I = list of integers
O = average integer
RULES
-list never empty
-all positive integers
E
D
list and integer
A
def variable "average"= sum of list modulo divided by len(list)
return
C
'''

def average(my_list):
    return sum(my_list) // len(my_list)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True