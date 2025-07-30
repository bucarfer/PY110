'''E1 Searching 101:
Write a program that solicits 6 numbers from the user and prints a message that describes wether the sixth number appears among the first five

##P
-Request 6 number digits from the user
-print message explaining if number is within previous numbers

Rules imp:
-repetition of the num in prev 5

Input: 6 different numeric strings
Output: Numeric string

Questions:
can the user enter another string that is not a n? no
assume numbers always 2 digits?

##E
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.

##D
strings and integers with list

##A
- Introduce 6 prompt asking user for 6 numbers
- add a variable to each input received and transform them to integers
- check if number 6 is equal to prev 5
- if yes -> string interpolation with "is in"
- if not -> isn't

##C
'''

n1 = int(input('Enter the 1st number: '))
n2 = int(input('Enter the 2nd number: '))
n3 = int(input('Enter the 3rd number: '))
n4 = int(input('Enter the 4th number: '))
n5 = int(input('Enter the 5th number: '))
n6 = int(input('Enter the last number: '))

number_list = [n1, n2, n3, n4, n5]
if n6 in number_list:
    identity = "is in"
else:
    identity = "isn't in"

print(f'{n6} {identity} {n1},{n2},{n3},{n4},{n5}')

##LsBot suggestions, use loop to avoid repetition, refer to list in f'string to dont list all numbers

number_list = ['1st', '2nd', '3rd', '4th', '5th']
numbers_selected = []

for ordinal in number_list:
    number = int(input(f'Enter the {ordinal} number: '))
    numbers_selected.append(number)

last = int(input(f'Enter the last number: '))

if last in numbers_selected:
    identity = "is in"
else:
    identity = "isn't in"

print(f"{last} {identity} {', '.join(str(n) for n in numbers_selected)}")

'''E2 - Palindrome:
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

P
input = string
output = Boolean

exp rules
- if palindrome return True, otherwise False
- case matters
- all char matters

imp
-num integers are allowed

E

test cases help me understand: all char matters
meaning spaces are relevant

D
we use string data

A
we create the reverse string
if the reverse string is = to the string the string is palindromic

C
'''

def is_palindrome(my_str):
    rev_str = my_str[::-1]
    if my_str == rev_str:
        return True
    else:
        return False

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

## LSbot comments, the comparison already returns a Boolean, we can simplify the code as:

def is_palindrome(my_str):
    rev_str = my_str[::-1]
    return my_str == rev_str

## it can even be reduced to one line:

def is_palindrome(my_str):
    return my_str == my_str[::-1]

'''E3 - Palindrome part 2:
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

P
input = string
output = Boolean

rules exp:
- True if palindrome
- False otherwise
- case-insensitive
-ignore non_alphanumeric char (skip)

E
example of only alphanumeric matters explains that non alphanumeric numbers are skipped without counting them in the comparisson like they didnt exist

D
strings

A
Create a new empty string
iterate throgh existing str and if alphanum add to new str
use casefold method for case insensitive and reverse new string
if equality condition new (reverse) = new (non reverse) return True

C
'''

def is_real_palindrome(my_str):
    new_str = ''
    for char in my_str:
        if char.isalnum():
            new_str += char
    return new_str.casefold()[::-1] == new_str.casefold()

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

## lsBot alternative simplify approach

def is_real_palindrome(my_str):
    new_str = ''
    for char in my_str:
        if char.isalnum():
            new_str += char.casefold()
    return new_str[::-1] == new_str

## most compact option

def is_real_palindrome(my_str):
    cleaned_str = ''.join(char.casefold() for char in my_str if char.isalnum())
    return cleaned_str == cleaned_str[::-1]

'''E4: Running totals:
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

P
input = list of numbers
output = list of numbers, each iterable is the addition

rules:
-return each element running total until that index

E
-explains all test cases are integers (no need to worry about other type of numbers)
-empty strings return empty strings without error
-single strings return single string

D
list of integers

A
create new list
iterate exist list, add addition result to new list index
return new list

C
'''

def running_total(my_lst):
    new_lst = []
    for idx in range(len(my_lst)):
        if idx == 0:
            new_lst.append(my_lst[idx])
        else:
            new_lst.append(new_lst[idx-1] + my_lst[idx])
    return new_lst

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

## lsBot suggestions, delete if/else by adding a new var total

def running_total(my_lst):
    new_lst = []
    total = 0
    for num in my_lst:
        total += num
        new_lst.append(total)
    return new_lst

'''E5: Letter counter (part1)
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

P
input = string
output = dict of len(words) -> values and repetition -> key

Rules
can consist on zero strings or multiple strings
strings are separated by spaces
non alpha char are also part of the string

E
examples help to explain the rules
an empty string will produce an empty dict

D
strings, lists, and dict

A
create an empty dict
separate string into words with method 'split' and define list var
iterate each word of the list and capture the len of the word
** assign len of the word to key dict, use def value 0
return dict

C
'''

def word_sizes(my_str):
    my_dict = {}
    my_list = my_str.split()

    for word in my_list:
        value = my_dict.get(len(word), 0)
        my_dict[len(word)] = value + 1

    return my_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

## lsBot suggestion to use var names more understandable

def word_sizes(text):
    count_dict = {}
    word_list = text.split()

    for word in word_list:
        value = count_dict.get(len(word), 0)
        count_dict[len(word)] = value + 1

    return count_dict

'''E6: Letter counter (part2)
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

P
same exercise but exclude non letters from count

A
create an empty dict
separate string into words with method 'split' and define list var
iterate each word of the list,
** create a new word with only alpha char with for loop
capture the len of the new word
assign len of the word to key dict, use def value 0
return dict

C
'''
def word_sizes(text):
    count_dict = {}
    word_list = text.split()

    for word in word_list:
        new_word = ''
        for char in word:
            if char.isalpha():
                new_word += char
        value = count_dict.get(len(new_word), 0)
        count_dict[len(new_word)] = value + 1

    return count_dict

#lsBot suggestion, solved it with a helper function and ignore words with all non alpha char

def word_cleaning(word):
    cleaned_word = ''
    for char in word:
        if char.isalpha():
            cleaned_word += char
    return cleaned_word

def word_sizes(text):
    count_dict = {}
    word_list = text.split()

    for word in word_list:
        new_word = word_cleaning(word)
        if new_word == '':
            continue
        value = count_dict.get(len(new_word), 0)
        count_dict[len(new_word)] = value + 1

    return count_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

'''E7: Letter swap
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

P

input = string of words
output = new string of words

rules explicit:
-return new string swapping the first for the last letter
-strings contain at least 1 letter and one word
-strings only contain letters and no extra spaces

E
- based on examples there it is case sensitive (keep cases as they are)

D
strings and lists

A
create an empty string
create an empty list
split string into list with -split() method
iterate each word of string and create a new string
    change 1st for last char of string
    keep rest char the same
join list words into a unique new string
return new string

C
'''
def swap(my_str):
    new_str = ''
    new_list = []

    my_list = my_str.split()

    for word in my_list:
        if len(word) == 1:
            new_str = word
        else:
            new_str = word[-1] + word[1:-1] + word[0]
        new_list.append(new_str)

    result = ' '.join(new_list)
    return result


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

## solution lsBot using a helper function

def swap_first_last(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]

def swap(my_str):
    word_list = my_str.split()
    # Now you can create the new list
    new_list = []
    for word in word_list:
        new_list.append(swap_first_last(word))

    return ' '.join(new_list)

## solution lsbot using a helper function and a list comprehension

def swap_first_last(word):
    if len(word) == 1:
        return word
    return word[-1] + word[1:-1] + word[0]

def swap(my_str):
    words = my_str.split()
    swapped_words = [swap_first_last(word) for word in words]
    return ' '.join(swapped_words)

'''E8: Convert string to a Number
Write a function that takes a string of digits and returns the appropriate numbers as an integer. You may not use standard constructors like int. your function should calculate the result using the characters in the string.

For now, do not worry about leading + o - signs, nor should worry about invalid characters, assume all char are numeric.

P
input = numeric string
output = integer

rules:
return integer of numeric string provided without using int()
you have to use the characters in the string
dont worry about leading + o - signs
numeric strings only

E

D
input = numeric string
output = integer
dict to map strings digits to integer digits

A
create a helper fnction with a dictionary with each numeric string has its integer value

in the main function
create a new integer
create a number with the length of the string -1
create an operation multiplying each unit by each 10 time value and adding all of them


## lSBot Algorithm correction:
1. Create a data structure (like a dictionary) that maps each numeric character from '0' to '9' to its integer equivalent (0 to 9).
2. Initialize a variable, `total_value`, to 0.
3. Initialize a variable, `power_of_ten`, to the length of the input string minus 1
4. Iterate through each `character` of the input string from left to right:
   a. Find the integer value of the `character` using the map from step 1. Let's call this `digit`.
   b. Calculate the place value: `digit * (10 ** power_of_ten)`.
   c. Add the result to `total_value`.
   d. Decrement `power_of_ten` by 1.
5. After the iteration is complete, return `total_value`.

'''

def str_to_int(my_str):
    my_dict = {}
    count = 0
    for num_str in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        my_dict[num_str] = count
        count += 1
    return my_dict[my_str]

def string_to_integer(my_str):
    my_int = 0
    decimal_number = len(my_str) - 1
    for char in my_str:
        my_int = (str_to_int(char) * 10 ** decimal_number) + my_int
        decimal_number -= 1
    return my_int

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

## lsBot suggestion, create dict as a constant variable and build the numbers directly with formula: value = (10 * value) + digit ; starting value 0

DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
}

def string_to_integer(my_str):
    value = 0
    for char in my_str:
        value = (10 * value) + DIGITS[char]

## additional exercise, Write a hexadecimal_to_integer function that converts a string representing a hexadecimal number to its integer value. Hexadecimal numbers use base 16 instead of 10, and the characters A, B, C, D, E and F (and the lowercase equivalents) correspond to decimal values of 10-15.

HEX_DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
}

def string_to_integer(my_str):
    value = 0
    for char in my_str:
        value = (16 * value) + HEX_DIGITS[char.upper()]
    return value

'''E9: Convert string to a Signed number
Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

P
input = numeric integer (includding signs + or -)
output = signed number

rules:
- return signed int if leading + or negative if leading -
- string always contains a valid number

E

D
strings, integers, and constant dict

A
use if conditions for negative numbers -> strings that start with char '-'
    remove leading char
    return int with string_to_integer function and add (-) sign
use else condition for positive numbers
    remove first char if it is a +
        return int with string_to_integer

'''

DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
}

def string_to_integer(my_str):
    value = 0
    for char in my_str:
        value = (10 * value) + DIGITS[char]
    return value

def string_to_signed_integer(my_str):
    if my_str[0] == '-':
        my_str = my_str[1:]
        return string_to_integer(my_str) * (-1)
    else:
        if my_str[0] == '+':
            my_str = my_str[1:]
        return string_to_integer(my_str)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

## minor suggestions lsBot, create if/elif/else (better structure) and use a more specific variable name my_str -> num_str:

def string_to_signed_integer(num_str):
    if num_str[0] == '-':
        num_str = num_str[1:]
        return - string_to_integer(num_str)
    elif num_str[0] == '+':
        num_str = num_str[1:]
        return string_to_integer(num_str)
    else:
        return string_to_integer(num_str)

## LS solution:

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)

'''E10: Convert a number to a string
Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

P
input = integer
output = numeric string

rules:
-only positive integers
-cant use constructors like int
-construct string by analyzing and manipulating the number

E

D
strings, integer and constant dict

A
- create a dictionary with an integer value for each string value
- create empty string
- transform integer to string with dict
- return string

C
'''

DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
}

NUM_STR = {value:key for key,value in DIGITS.items()}

def integer_to_string(num):
    my_str = ''
    if num == 0:
        my_str = '0'

    while num > 0:
        my_str += NUM_STR[num % 10]
        num = num // 10

    return my_str[::-1]

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

## lsBot suggestions, good solution but can be siplified with:

NUM_STR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(num):
    my_str = ''

    while num > 0:
        remainder = num % 10
        my_str = NUM_STR[remainder] + my_str
        num = num // 10

    return my_str or '0'

'''E11: Convert a signed number to a string

'''

# In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

# Write a function that takes an integer and converts it to a string representation.

# You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.

'''
P
I =  integer
O = numeric string

rules:
- adding the ability to represent negative numbers as well.

E
add + even if it signed is not included in integer number

A
take integer
transform with function to string
    change helper function to remove negative sign

inside main function create different options:
    if num < 0:
        '-' + helper function
    elif num > 0:
        '+' + helper function
    else:
        '0''

'''

NUM_STR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(num):
    my_str = ''

    if num < 0:
        num = -num

    if num == 0:
        my_str = '0'

    while num > 0:
        my_str += NUM_STR[num % 10]
        num = num // 10

    return my_str[::-1]

def signed_integer_to_string(num):

    if num < 0:
        result = '-' + integer_to_string(num)
    elif num > 0:
        result = '+' + integer_to_string(num)
    else:
        result = '0'
    return result

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

## lsBot, try to dont change the helper function from the previous exercise and handle the negative numbers in a different way

NUM_STR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(num):
    my_str = ''

    while num > 0:
        remainder = num % 10
        my_str = NUM_STR[remainder] + my_str
        num = num // 10

    return my_str or '0'

def signed_integer_to_string(num):

    if num < 0:
        result = '-' + integer_to_string(-num)
    elif num > 0:
        result = '+' + integer_to_string(num)
    else:
        result = '0'

    return result