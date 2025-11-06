### Problem 1 - solved in 15min

# Create a function that takes a list of numbers as an argument. For each number, determine how many numbers in the list are smaller than it, and place the answer in a list. Return the resulting list.

# When counting numbers, only count unique values. That is, if a number occurs multiple times in the list, it should only be counted once.

'''
P
take a list of numbers and return another list counting how many numbers are smaller than each one (unique)
E
-[8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2]
- if list has one element - result will be a list with the num 0
I = list of integers
O = list of integers (same lenght) -> counting unique smaller numbers

lists and maybe sets (for unique)
A
-iterate through list and compare to rest of elements
    if element is less and unique, count + 1
        append result to new list
return new list
C'''
def smaller_numbers_than_current(my_list):
    new_list = []
    for i in my_list:
        count = 0
        for j in set(my_list):
            if j < i:
                count += 1
        new_list.append(count)

    return new_list

## using list comprehension instead

def smaller_numbers_than_current(my_list):
    return [len([j for j in set(my_list) if j < i]) for i in my_list]

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

### Problem 2 - solved in 20min - find it hard **
# Create a function that takes a list of integers as an argument. The function should return the minimum sum of 5 consecutive numbers in the list. If the list contains fewer than 5 elements, the function should return None.

'''P
E
- if list len < 5 -> return None
- return min sum of 5 consecutive numbers
I = list of integers (positive or negative)
O = integer (sum of 5 consecutive list)
D
lists and integers
A
-first check if len(list) < 5:
    if so -> return None
- with list comprehension create a list with the summary of all the 5 len lists possible
    return min value of this new list
C
'''
def minimum_sum(my_list):
    if len(my_list) < 5:
        return None

    return min(sum(my_list[j] for j in range(i, i + 5)) for i in range(len(my_list) - 4))


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

## lsBot suggestions to keep it more simple:
# use slicing to create the new list with len 5 instead of a inner loop

def minimum_sum(my_list):
    if len(my_list) < 5:
        return None

    return min(sum(my_list[i:i+5]) for i in range(len(my_list) - 4))

### Problem 3 - solved in 20min
# Create a function that takes a string argument and returns a copy of the string with every second character in every third word converted to uppercase. Other characters should remain the same.

'''
P
take stirng and return new string with every third word
    EVERY second char -> upper()
I = string
O = new string
E
-if upper -> remains upper
D
list
A
-convert string into list of strings. -> .split()
-use list comprehension
    filter with if condition (third word, outer loop) 2, 5,
        return inner loop -> for char in enumerate(word) if idx % 2 == 0 char.upper(), rest else
    rest use else expresion
-return join version -> .join(list)
C'''

def to_weird_case(my_str):
    my_list = my_str.split()

    return ' '.join([''.join([char.upper() if idx in range(1, 200, 2) else char for idx, char in enumerate(word)]) if idx in range(2, 200, 3) else word for idx, word in enumerate(my_list)])

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

## lsBot solution suggestion:
# using a helper function to make the code more clear
# using modulo operations % 2 and % 3 to dont have a limit of items like I have in the range version (harder to get to the right modulo and remainder)

# How to approach this generally 1) Identify the period (N): how often does the pattern repeat? 2) Identify the offset (r): at which index in that cycle should it trigger? Use a few examples to find r. 3) Use modulo: i % N == r.

# alternative for i in range(2, len(words), 3)

def to_weird_case(s):
    words = s.split()

    def transform_word(word):
        return ''.join(
            ch.upper() if ci % 2 == 1 else ch
            for ci, ch in enumerate(word)
        )

    return ' '.join(
        transform_word(w) if wi % 3 == 2 else w
        for wi, w in enumerate(words)
    )

***### Problem 4 - solved in 23min (slightly over)
# Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

'''P
E
- multiple numbers with same difference - return the first
- couple of int do not need to be consecutive
I = list of integers
O = tuple of 2 integers (closest int in value)
D = lists and tuples
A
- use brute force to iterate through all pair possibilities
only replace if num1 - num2 < prev pair -> absolute value
- outer loop for first in range(len(list))
    inner loop for second in range(first + 1, len(list))
        outer expression (first, second)
(num1 - num2) for num1, num2 in list
min(prev_list) -> use index with value obtained -> return tuple pair with that index
C'''

def closest_numbers(my_list):
    tup_list = [(my_list[num1], my_list[num2]) for num1 in range(len(my_list)) for num2 in range(num1 + 1, len(my_list))]
    dif_list = [abs(num1 - num2) for num1, num2 in tup_list]
    idx_value = dif_list.index(min(dif_list))
    return tup_list[idx_value]

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

## lsBot fastest way without building all couples in a list

def closest_numbers(nums):
    best_pair = None # starting value for pairs
    best_diff = float('inf') # infinite
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            d = abs(nums[i] - nums[j])
            if d < best_diff:       # strict < preserves the first pair on ties
                best_diff = d
                best_pair = (nums[i], nums[j])
    return best_pair

***### Problem 5 - solved in 27min
# Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

'''
P
E
- if same frequency, return 1st one
- case insensitive
I = string
O = character (most frequent)
D
set and list
A
- new_list = char.lower() for char in string if char.isalnum()
- ['char'] = 0 for char in set(new_list)
- ['char'] += 1 for char in new_list
- max(list(dict.values())) -> max value of dict
- key for key, value in dict.items() if value == max
- return key
C
'''

def most_common_char(my_str):
    new_list = [char.lower() for char in my_str]
    my_dict = {char: new_list.count(char) for char in new_list}
    max_count = max(list(my_dict.values()))

    for key, value in my_dict.items():
        if value == max_count:
            return key

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

## lsBot suggestions:
# you dont need to create a list, you can count and iterate the string directly
# you can iterate the lowercase string directly and return the first character with max_count

def most_common_char(my_str):
    my_dict = {char: (my_str.lower()).count(char) for char in my_str.lower()}

    max_count = max(list(my_dict.values()))

    for char in my_str.lower():
        if my_dict[char] == max_count:
            return char