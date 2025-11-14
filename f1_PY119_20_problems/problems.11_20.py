***### Problem 11 - 25min (hardest one so far)
# Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

# You may assume that the string argument consists entirely of lowercase alphabetic letters.

'''
P
I = non empty lowercase string # (s)
O = tuple(substr, integer) # (t, k) -> s == t * k
R
- strings are formed by unique strings or subst repeated
- no multiple substrings in between more characters
- no empty strings allowed and always lowercase-alpha characters
- single char 1st choice -> my_str[0:1]
- s == t * k
E
('xyz xyz xyz') -> substr always start with first character of string
    -> therefore we want all ending substrings
D
strings and slice
A
idea - create all end substrings of string and check if they appear in the rest of the string (repetition)
main
-create all substrings -> for i in range(len(my_str))
    -> my_str[:i + 1] # (missing las character to check at the end)
-calculate possible value of k -> len(my_str) // len(my_str[:i + 1])
    if s == t * k:
        return(t, k) #the smallest the subst, the highes repetition
C
'''

def repeated_substring(s):
    for i in range(len(s)):
        if len(s) % len(t) != 0: # this line checks remainder is 0 (not really needed but better O(n))
            continue
        t = s[:i + 1]
        k = len(s) // len(t)
        if s == t * k:
            return (t, k)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

### Problem 12 - 12min
# Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

# Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

'''P
E
-case insensitive
-additional char non alpha -> ignore
I = string
O = Boolean (True if pangram)
D
list and set
A
alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    use list comprehension to filter only alpha char and transform to lower()
        -> transform to set

transform back to string and compare to set(alphabet_string)

C
'''

def is_pangram(my_str):
    alphabet_string = 'abcdefghijklmnopqrstuvwxyz'
    return set([char.lower() for char in my_str if char.isalpha()]) == set(alphabet_string)


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard's job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard's task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard's job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

## lsBot suggestions
# use a set comprehension directly
# keep constant of alphabet outside the function

ALPHABET = set('abcdefghijklmnopqrstuvwxyz')

def is_pangram(my_str):
    return {char.lower() for char in my_str if char.isalpha()} == ALPHABET

## even shorter, knowing that alphabet is 26 characters

def is_pangram(my_str):
    return len({char.lower() for char in my_str if char.isalpha()}) == 26

///### Problem 13 - 11min - DICTIONARY PRACTICE
# Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

# You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

'''
P
I = 2 strings (source, target)
O = Bool -> true if some portion of the source ca be rearranged to match target
R
-strings only contain lowercase and alpha characters
-Neither string will be empty
E
-string can contain more characters than target
-all characters of target must be in source including DUPLICATES
D
list and strings
A - wrong algo (need a dictionary)
-create a list of characters in first string that appear in second
    list comprehension
-if len(new_list) >= len(target) -> True
    else False
C
'''
def unscramble(my_str, target):
    return len([char for char in my_str if char in target]) >= len(target)

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

## lsBot, for examples like source: 'abccc', target: 'aacc' does not work my previous algo and code, we need to use dictionaries

'''
D
strings and dictionaries
A
create 2 dictionaries
- one with source and one with target
- iterate through characters of target:
    if char count in source < count char in target:
        return False
- return True
'''
from collections import Counter

def unscramble(source, target):
    source_dict = Counter(source)
    target_dict = Counter(target)

    for char in target:
        if source_dict[char] < target_dict[char]: # if char does not exist in source_dict it returns 0 instead of giving us a keyerror because it is a Counter dict
            return False

    return True


## now we do it again without using Counter to practice dictionaries

def unscramble(source, target):
    source_dict = {}
    for ch in source:
        source_dict[ch] = source_dict.get(ch, 0) + 1

    target_dict = {}
    for ch in target:
        target_dict[ch] = target_dict.get(ch, 0) + 1

    for char, count in target_dict.items():
        if source_dict.get(char, 0) < count:
            return False

    return True

### Problem 14 - 8min
# Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

# For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

# If the argument is negative, return 0.

'''P
I = integer
O = integer (sum of all num less than argument multiples of 7 OR 11)
R
-if arg is negative -> return 0
-if arg is 0 -> return 0
E
D
integer and list comp
A
idea create a list with all multiples of 7 or 11 below the arg and return the sum
- loop through range(num)
    if num % 7 == 0 or num % 11 == 0
        out exp -> num
- return the sum
C'''

def seven_eleven(my_int):
    if my_int < 0:
        return 0
    return sum(num for num in range(my_int) if num % 7 == 0 or num % 11 == 0)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

### Problem 15 - 15min + 5min(optB)
# Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

'''P
I = numeric string
O = integer (greatest product of 4 consecutive digits)
R
-arg will always have more than 4 digits
E

D
strings, int, list
A
-create all subst of 4 characters -> i range(len(my-str) - 4)  # example 5 - 4 = 1
    -> out expr int(my_str[i + 1]) * int(my_str[i:i + 2]) * int(my_str[i:i + 3]) * int(my_str[i:i + 4])
-return max
C'''

def greatest_product(my_str):
    return max([int(my_str[i]) * int(my_str[i + 1]) * int(my_str[i + 2]) * int(my_str[i + 3]) for i in range(len(my_str) - 4 + 1)])

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

## opt B, trying to make it easier to read:

def greatest_product(my_str):
    my_lst = [my_str[i: i + 4] for i in range(len(my_str) - 4 + 1)]
    return max(int(a) * int(b) * int(c) * int(d) for a, b, c, d in my_lst)

## lsBot minor improvements for both solutions

# solution A, simplify name str, use generator, and 3 instead of - 4 + 1

def greatest_product(s):
    return max(
        int(s[i]) * int(s[i+1]) * int(s[i+2]) * int(s[i+3])
        for i in range(len(s) - 3)
    )

# solution B, use a generator directly to avoid list

def greatest_product(s):
    return max(
        int(a) * int(b) * int(c) * int(d)
        for a, b, c, d in (s[i:i+4] for i in range(len(s) - 3))
    )

def greatest_product(s):
    return max(
        int(a) * int(b) * int(c) * int(d)
        for i in range(len(s) - 3)
        for a, b, c, d in [s[i:i+4]]
)

### Problem 16 - 11min - OPT B and C with dict O(n) 5min
# Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

'''P
I = string (alphanumeric) # either all num or all alpha
O = integer (count of char or digits that occur more than once)
R
-case insensitive (transform to lowercase)
-it counts the same a char that appears 2 times than 5 times
E
D
strings
A
- init count = 0
- loop through set of string.lower # set to avoid duplicates
- if count char > 1
    count += 1
- return count
C'''

def distinct_multiples(my_str):
    count = 0
    s = my_str.lower()

    for char in set(s):
        if s.count(char) > 1:
            count += 1

    return count

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

## solve with dictionary without count -> O(n) version

def distinct_multiples(my_str):
    d = {}
    s = my_str.lower()

    for char in s:
        d[char] = d.get(char, 0) + 1

    return sum(1 for value in d.values() if value > 1)

print(distinct_multiples('xxyypzzr'))

## simplify version using Counter

from collections import Counter

def distinct_multiples(my_str):
    d = Counter(my_str.lower())
    return sum(1 for value in d.values() if value > 1)

***### Problem 17 - 40min (hard to understand how to check prime number and for...: else:)
# Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

# Notes:

# The list will always contain at least 2 integers.
# All values in the list must be positive (> 0).
# There may be multiple occurrences of the various numbers in the list.

# prime numbers can be only divided by themselves or 1


'''P
I = list of positive integers (at least 2, can be same integer)
O = integer (smallest num to append to list for nearest prime num)
R
- search for nearest prime number
E
D
list and integers
A
-init count = 1
-calculate start_num = sum(my_list)
- possible_prime = start_num + count
- if prime:
    return count

while True:
    count += 1
    start_num += count # 8
    for div in range(2, start_num):
        if start_num % div == 0:
            break
    else:
        return count
C
'''

def nearest_prime_sum(my_list):
    count = 0
    start_num = sum(my_list)

    while True:
        count += 1
        pos_prime = start_num + count #7 + 1 -> 8
        for div in range(2, pos_prime): # [2, 3, 4, 5, 6, 7]
            if pos_prime % div == 0:
                break # exists the for loop (number is NOT prime)
        else:
            return count # (only runs if for loop finished -> prime number)

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

# 🧠 TL;DR: How to Think About It
# Structure	Meaning
# if ...: else:	Classic conditional: one thing or the other
# for ...: else:	“Do this if the loop didn't break.”
# while ...: else:	Same as above, for while-loops

## version without else statement using boolean flag

def nearest_prime_sum(my_list):
    count = 0
    start_num = sum(my_list)

    while True:
        count += 1
        pos_prime = start_num + count
        is_prime = True  # Assume it's prime until proven otherwise

        for div in range(2, pos_prime):
            if pos_prime % div == 0:
                is_prime = False  # Found a divisor → not prime
                break  # No need to keep checking

        if is_prime:
            return count

# using a helper function -> is_prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime_sum(nums):
    total = sum(nums)
    candidate = total + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate - total

# helper function optimization
#√n = n**0.5

def is_prime(n):
    if n < 2:
        return False
    limit = int(n**0.5 + 1)
    for i in range(2,limit): # it loops ony √n times
        if n % i == 0:
            return False
    return True

### Problem 18 - 14min
# Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

# If you are given a list with multiple answers, return the index with the smallest value.

# The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

'''P
I = list of integers
O = integer (index N)
R
-N sum(list[:N]) == sum(list[N + 1:])
- if no N -> return -1
- if multiples N -> return smallest N
E
D
list and slicing
A
-loop with all indexes of len(my_list)

    -if sum(my_list[:i]) == sum(my_list[i +1:]):
        return i

return -1
C'''

def equal_sum_index(my_list):
    for i in range(len(my_list)):
        if sum(my_list[:i]) == sum(my_list[i + 1:]):
            return i

    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

## lsBot optimized O(n) version:

def equal_sum_index(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        right = total - left - x
        if left == right:
            return i
        left += x
    return -1

### Problem 19 - 6min
# Create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times. There will always be exactly one such integer in the input list.

'''P
I = list of integers
O = integer that appears odd number of times
R
-there will be always a integer that appears an odd amount
E

D
integers, list, and set
A
idea iterate over set version of list
    if count of num % 2 != 0
        return num
C
'''

def odd_fellow(my_list):
    for num in set(my_list):
        if my_list.count(num) % 2 != 0:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

##elegant way using XOR
# | Operation       | Result                  |
# | --------------- | ----------------------- |
# | `x ^ x`         | `0`                     |
# | `x ^ 0`         | `x`                     |
# | Associative law | Order doesn’t matter    |
# | Commutative law | Grouping doesn’t matter |

def odd_fellow(my_list):
    result = 0
    for num in my_list:
        result ^= num
    return result

### Problem 20 - 4min - opt B 2min - opt C 3min
# Create a function that takes a list of numbers, all of which are the same except one. Find and return the number in the list that differs from all the rest.

# The list will always contain at least 3 numbers, and there will always be exactly one number that is different.

'''P
I = list of integers (all the same except one)
O = unique num
R
-there will be always at least 3 num
-only one dif num
E
D
integers, list, set
A
iterate over set and return num that appears only one (method .count())
C'''

def what_is_different(my_list):
    for num in set(my_list):
        if my_list.count(num) == 1:
            return num

## opt B, using a frequency dict with Counter

from collections import Counter

def what_is_different(my_list):
    my_dict = Counter(my_list)
    for item, num in my_dict.items():
        if num == 1:
            return item

## op C, without counter or count

def what_is_different(my_list):
    my_dict = {}

    for num in my_list:
        my_dict[num] = my_dict.get(num, 0) + 1

    for num, count in my_dict.items():
        if count == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

## bonus - one liner with Counter

def what_is_different(my_list):
    return next(n for n, c in Counter(my_list).items() if c ==1)