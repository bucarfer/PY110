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
