"""
PROBLEM EXAMPLE 1:

Given a string, write a function `change_me` which returns the same
string but with all the words in it that are palindromes uppercased.
"""

# Comments show expected return values
change_me("We will meet at noon")       # "We will meet at NOON"
change_me("No palindromes here")        # "No palindromes here"
change_me("")                           # ""
change_me("I LOVE mom and dad equally") # "I LOVE MOM and DAD equally"

# input: string
# output: string (not the same object)
# rules:
#   Explicit requirements:
#     - Every palindrome in the string must be converted to uppercase.
#       (Reminder: a palindrome is a word that reads the same forwards
#       and backward).
#     - Palindromes are case sensitive. ("dad" is a palindrome, but "Dad" is not.)

#   Implicit requirements:
#     - If the string is an empty string, the result is an empty string.

def change_me(my_string):
    my_list = my_string.split()
    for word in my_list:
        if word[0] == word[-1]:
            word = word.upper()
            new_string = ' '.join(my_list)
            return new_string

"""
PROBLEM EXAMPLE 2:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

# Test cases:

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

# input: string
# output: list of palindrome substring (not the same object)
# rules:
#   Explicit requirements:
#     - Palindromes detetection (case sensitive. abBA != palindrome)
#     - return substrings palindromes as list elements
#     - min len substring (2 char)

#   Implicit requirements:
#     - If the string is an empty string, the result is an empty list.
#     - if the string doesnt have any palindromes, the result is an empty list.

# Algorithm:
#   - Declare a result variable and initialize it to an empty list.
#   - Create a list named substr_list that contains all the substrings
#     of the input string that are at least 2 characters long.
#   - Loop through the words in the substr_list list.
#   - If the word is a palindrome, append it to the result list.
#   - Return the result list.

### LESSON 11, PROBLEM EXAMPLE.

'''PART 1, UNDERSTANDING PROBLEM

Leftover Blocks
You have a number of building total_blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building total_blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four total_blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between total_blocks.
Write a program that, given the number of available total_blocks, calculates the number of total_blocks left over after building the tallest possible valid structure.

Tasks
You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.'''

# Input: integer
# Output: integer (reminder of leftover total_blocks after building tallest structure)

# explicit rules:
# -1 block is 1 integer (cubes with square faces)
# - top layer is single Block (1 integer unit)
# - each block must be supported by 4 total_blocks
# - each block in lower layer can support more than one block in an upper layer

# implicit rules:
# -the second tallest layer will have 4 total_blocks (4 integer units)
# -the third tallest layer will be 3 by 3 total_blocks to create a bigger rectangle (9 integer units)
# -the fourth layer will be 4 by 4 (16 total_blocks)
# - therefore layer number * layer number = number of total_blocks of layer

# Questions:
# I assume we will always receive integer numbers (no decimals leftover)
# We use the minimum number of total_blocks per layer

'''PART 2, TEST CASES PROVIDED

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True'''

'''PART 3, DATA STRUCTURE'''

# I will use integers and arithmetic operations

'''PART 4, ALGORITHM'''

# building layers from top to bottom
# while layer*layer <= reminder:
# starter layer -> 1
# line 1 == total_blocks - layer*layer == reminder
# next loop layer increases by one
# when reminder < layer*layer return reminder

'''BASED ON YOUR NOTES AND ALGORITHM IMPLEMENT CODE'''

def calculate_leftover_blocks(total_blocks):
    layer = 1

    while layer * layer <= total_blocks:
        total_blocks = total_blocks - layer * layer
        layer += 1

    return total_blocks

### LESSON 12, PROBLEM EXAMPLE.

'''PART 1 UNDERSTANDING PROBLEM:
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains and return the sorted list. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

Tasks
You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.'''

# input = list of strings
# output = list of strings (ordered by adjacent consonants only)

# explicit:
# -ordered based on highest number of adjacent consonants a string contains
# -if 2 strings contain same n of adjacent consonants, keep the original order
# -adjacent consonants -> next two each other or separated by space between 2 words

# implicit:
# -strings can have multiple words

#Questions:
# - is the order ascending or descending?
# - should I handle case sensitivity?

'''PART 2: TEST CASES

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']'''

#the test provided help me understand that the ASCI value of the consonants doesn't matter, only the number of adjacent consonants as explained in the problem description
#also helps understand that we dont need to deal with characters that are not part of the english alphabet

#Questions answered by test cases:
# - is the order ascending or descending? descending
# - should I handle case sensitivity? no

'''PART 3: DATA STRUCTURE'''

# I will be using dictionaries, adding a integer value to each strings.
# I will have to iterate over the list elements and string characters.
# the final result will be a list created from the dictionary view object.

'''PART 4: ALGORITHM'''

# 1.create an empty dictionary
# 2.evaluate how many adjacent consonants has each list element (string) with help function
# 3.add the element to the empty dictionary with the strings as keys and the number of consonants as the values
# 4.order the dictionary by values
# transform the values view object to a list and return the value

# 1. help function counting consonants per string
# 2. iterate through string and if a char is a consonant add 1 unit to the count
# 3. if the next iteration is a vowel change the count to 0
# 4. replace total count by count if total count is 0 or smaller than count
# 5. at the end, if the total count is 1 change it to 0 to dont count with single consonant characters
# 6. return total count

'''PART 5: CODING'''

def count_consonant(my_string):
    total_count = 0
    count = 0

    for char in my_string:
        if char not in 'aeiou ':
            count += 1

        if char in 'aeiou':
            count = 0

        if total_count == 0 or total_count < count:
            total_count = count

    if total_count == 1:
        total_count = 0

    return total_count

def sort_by_consonant_count(my_list):
    my_dict = {}

    for my_string in my_list:
        count = count_consonant(my_string)
        my_dict[my_string] = count

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    return list(sorted_dict.keys())


# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']

###LSbot tells me that it is much easier to keep the original list and sort it out with the keys of the consonant.
### Simpler solution using sort

def sort_by_consonant_count(my_list):
    my_list.sort(key=count_consonant, reverse=True)
    return my_list

def count_consonant(my_string):
    total_count = 0
    count = 0

    for char in my_string:
        if char not in 'aeiou ':
            count += 1

        elif char in 'aeiou':
            count = 0

        if total_count == 0 or total_count < count:
            total_count = count

    if total_count == 1:
        total_count = 0

    return total_count