'''PROBLEM 1: Inverting Dictionary
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.
'''

def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

'''PROBLEM 2: Retain Specific keys
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for the specified keys.

P
I = DICT and list of filter keys
O = new dict with selected keys
R
as explained in I and O
E
D
dict and lists
A
create a dict comprehension
iterate through input_dict and add to new dictionary only if it is part of keys list
C
'''

def keep_keys(input_dict, keys):
    return {key: value for key, value in input_dict.items() if key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

'''PROBLEM 3: Delete Vowels
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.
P
I = list of strings
O = new list of strings without vowels
R
- vowels = 'aeiou'
- as described in I and O
E
-if all vowels string in new list will be empty
-case sensitive
see below
D
list and strings
A
iterate through current list
    new_string = ''
    new_list = ''
    inner loop of char -> if char not in vowel -> add to new string
    append new_string to new_list

return new_list
C
'''

def remove_vowels(original):
    vowels = 'aeiouAEIOU'
    new_lst = []
    for my_str in original:
        new_str = ''
        for char in my_str:
            if char not in vowels:
                new_str += char
        new_lst.append(new_str)

    return new_lst

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

## LSBOT suggestion, transform inner loop in list comprehension and use cap_letters for constants

def remove_vowels(original):
    VOWELS = 'aeiouAEIOU'
    new_lst = []
    for my_str in original:
        new_lst.append(''.join([char for char in my_str if char not in VOWELS]))

    return new_lst

## reducing it to 2 comprehension lists with help function

def no_vowels_str(my_str):
    VOWELS = 'aeiouAEIOU'
    return ''.join([char for char in my_str if char not in VOWELS])

def remove_vowels(original):
    return [no_vowels_str(my_str) for my_str in original]

## single nested comprehension list -> too complicated to read, but tested...

def remove_vowels(original):
    VOWELS = 'aeiouAEIOU'
    return [''.join([char for char in my_str if char not in VOWELS]) for my_str in original]

'''PROBLEM 4: How long are you?
Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.
P
I = string
O = list of strings + space + n of characters
R
E
-examples below understood
-all examples are in lowercase
-if arguments is empty string or no agurment -> return empty list
D
string and lst
A
- first separate strings with split and space separator
- loop through list to create a new list with a list comprehension
    -> string + len(str)
C
'''

def word_lengths(words=None, default=''):
    if words is None:
        words = default

    list_words = words.split()
    return [f'{word} {len(word)}' for word in list_words]


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

## LS solution

def word_lengths(string=''): ## different way of handling no arguments
    if not string:
        return []

    return [f"{word} {len(word)}"
            for word in string.split()]

'''PROBLEM 5: List element multiplication
Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.
P
I = 2 list of integers
O = 1 list -> product of both
R
- list have same length
E

D
lists and integers. zip will create an iterator of tuples
A
1. Define a function multiply_items that accepts two lists, list_a and list_b.
2. Create a new list by iterating through pairs of elements from list_a and list_b. The zip function is perfect for creating these pairs.
3. For each pair (a, b), calculate their product, a * b.
4. Collect all the resulting products into the new list. A list comprehension is a great way to do this.
5. Return the new list.
C
'''

def multiply_items(list_a, list_b):
    return [a * b for a, b in zip(list_a, list_b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

## LSBOT ALTERNATIVE, loop iterating through both lists and append the multiplication of both indexes into a new list

def multiply_items(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])

    return result

'''PROBLEM 6: Sum of Sums
Write a function that takes a list of numbers and returns the sum of the sums of each leading subsequence in that list. Examine the examples to see what we mean. You may assume that the list always contains at least one number.
P
I = list of numbers
O = sum of sums of leading subsequence
R
list always contains at least one number
E
D
lists and subsequence
A
create new list
list comprehension to create all different leadings subs
    add new siblists to new list
return summary of new list elements
C
'''

def sum_of_sums(my_list):
    total = []
    [total.extend(my_list[:(idx + 1)]) for idx in range(len(my_list))]

    return sum(total)

print(sum_of_sums([3, 5, 2])  == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

## lsBot corrections -> dont use list comprehensions for side effects (mutating existing lists in place)

''' AMENDED PEDAC A
1. Initialize a new var called all_num
2. Iterate input using indexing
3. subsequence will be built from the beginning of the input until the current index
4. add subsequence to all_num var
5. after loop os finised return the sum of all_num list
'''

def sum_of_sums(my_list):
    all_num = []
    for idx in range(len(my_list)):
        sub_seq = my_list[:(idx + 1)]
        all_num.extend(sub_seq)

    return sum(all_num)

##LS solution

def sum_of_sums(numbers):
    total_sum = 0
    running_sum = 0
    for num in numbers:
        running_sum += num # 3 -> 8 -> 10
        total_sum += running_sum # 3 -> 11 ->21

    return total_sum

# ([3, 5, 2])

'''PROBLEM 7: Sum of Digits

Write a function that takes one argument, a positive integer, and returns the sum of its digits.
P
I = integer
O = sum of digits
R
E = see bellow
D
integers -> convert to list of strings
A
0. def sum_var
1. transform int to str
2. add the int of each char to sum_var in for lopp
3. return sum_var
C
'''

def sum_digits(num):
    sum_var = 0
    my_str = str(num)
    for char in my_str:
        sum_var += int(char)

    return sum_var

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

## lsBot suggestion use list comprehension

def sum_digits(num):
    return sum([int(char) for char in str(num)])
    # sames as return sum(int(char) for char in str(num)) generator expression

'''PROBLEM 8: STAGGERED CASE (part 1)
Write a function that takes a string as an argument and returns that string with a staggered capitalization scheme. Every other character, starting from the first, should be capitalized and should be followed by a lowercase or non-alphabetic character. Non-alphabetic characters should not be changed, but should be counted as characters for determining when to switch between upper and lower case.
P
I = string
O = new string with staggered caps
R
-starting from 1st, everty other char -> capitalization
-other characters: lower or non alpha
-non alpha char shoudlnt change but count for the staggering (includding spaces)

E
-empty stings return empty strings as shown below
D
strings -> list -> .join -> str
A
def str_var
loop over string and if idx % 2 == 0 -> uppercase() char
    if idx % 2 == 1 -> lowercase char
non alpha char will not be affected
this can be done with a list comprehension and join after witht the method .join
C
'''

def staggered_case(my_str):
    return ''.join(my_str[idx].upper() if idx % 2 == 0 else my_str[idx].lower() for idx in range(len(my_str)))


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

## corrected PEDAC
'''
1.Create an empty list to hold the new characters.
2.For each character and its index in the input string: a. If the index is even, convert the character to uppercase and add it to the list. b. If the index is odd, convert the character to lowercase and add it to the list.
3.Join the characters in the list into a single string.
4.Return the resulting string.'''

## Using enumerate instead

def staggered_case(my_str):
    return ''.join(char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(my_str))

'''PROBLEM 9: Staggered Case (part 2)
Modify the function from the previous exercise so it ignores non-alphabetic characters when determining whether it should uppercase or lowercase each letter. The non-alphabetic characters should still be included in the return value; they just don't count when toggling the desired case.
P
I = str
O = new_list staggered cap
R
-non alpha char do not count for staggered
-they need to be included in new string
E
D
str
A
def count = 0
def new_list = ''
for char in str -> if char is alpha -> add count to new_list
        count += 1
    if char is not alpha -> add * to new_list

for idx, char in enumerate(new_list)
    if char % 2 == 0:
        add str[idx].upper() to final result
    elif char % 2 == 1:
        add str[idx].lower() to final result
    else:
        add str[idx] to final result

return result
C
'''

def staggered_case(my_str):
    count = 0
    new_list = []
    for char in my_str:
        if char.isalpha():
            new_list.append(count)
            count += 1
        else:
            new_list.append('*')

    final_word = ''
    for idx, item in enumerate(new_list):
        if str(item).isdigit() and item % 2 == 0:
            final_word += my_str[idx].upper()
        elif str(item).isdigit() and item % 2 == 1:
            final_word += my_str[idx].lower()
        else:
            final_word += my_str[idx]

    return final_word


# def staggered_case(my_str):
#     return ''.join(char.upper() if idx % 2 == 0 else char.lower() for idx, char in enumerate(my_str))

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

## lsbot, try to use a single loop and add a variable that starts as True

## new algorithm
'''
A
1. def new empty string variable
2. def new state var and initialize as True
3. loop through all characters checking if the char is alpha
    4. If it use make_upper to decide case
    5. flip state var to false
    6. if the char is non alpha should be added directly without using make_upper

return result
'''

def staggered_case(my_str):
    final_word = ''
    make_upper = True
    for char in my_str:
        if char.isalpha():
            if make_upper:
                final_word += char.upper()
                make_upper = False
            else:
                final_word += char.lower()
                make_upper = True
        else:
            final_word += char

    return final_word

##LS solution

def staggered_case(string):
    result = ''
    upper = True

    for char in string:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char

    return result

'''PROBLEM 10: Remove consecutive duplicates
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.
P
I = list
O = list without consecutive eq char
R
E
- consecutive equal char are removed
D
list
A
loop through the list and check prev char and if it is equal -> skip
C
'''

def unique_sequence(my_list):
    new_list = []

    for idx in range(len(my_list)):
        if idx == 0:
            new_list.append(my_list[0])
        else:
            if my_list[idx] == my_list[idx-1]:
                continue
            else:
                new_list.append(my_list[idx])

    return new_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

## New code following new lsBot suggestions for algorithm

'''new algorithm
1. Define a function that accepts one argument, my_list.
2. Create an empty list called new_list to store the results.
3. Check if my_list is empty. If so, return new_list.
4. Add the first element of my_list to new_list.
5. Iterate through my_list starting from the second element.
6. On each iteration, compare the current element to the previous element.
7. If they are not the same, append the current element to new_list.
Return new_list.
'''

def unique_sequence(my_list):
    new_list = []
    if my_list == []:
        return new_list

    new_list.append(my_list[0])

    for idx in range(1, len(my_list)):
        if my_list[idx] != my_list[idx-1]:
            new_list.append(my_list[idx])

    return new_list

# LS solutions:

def unique_sequence(numbers):
    if not numbers:
        return []

    unique = [numbers[0]]
    for value in numbers[1:]:
        if value != unique[-1]:
            unique.append(value)

    return unique

## best one with list comprehension

def unique_sequence(numbers):
    return [value
            for idx, value in enumerate(numbers)
            if idx == 0 or value != numbers[idx -1]]