'''PROBLEM 1: ROTATION (PART 1)

Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.
P
I = list (ideal case)
O = new list -> rotate prev list
R
-do not mutate original list
-if no list -> return None
-if empty list -> return empty list
E
-lists of one item do not change
D
lists
A
1. check if not list -> return None
2. return new list, move first item to end with slicing
C
'''
def rotate_list(my_list):
    if not isinstance(my_list, list):
        return None

    return my_list[1:] + my_list[0:1] # my_list[0:1] same as [my_list[0]]

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) ==  [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

'''PROBLEM 2: Rotation (part 2)
Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.
P
I = integer, n of digits
O = new integer with end n of digits
R
-move first of the digits affected to the end (rest to the left)
E
-1 digit doesn't affect the number
D
-integers and slicing
A
0. handle edge case of 1 digit
1. transform integer to numeric string
2. take last digits from 2nd parameter with slice
3. add them back following rules with slicing
4. transform back to integer
C
'''

def rotate_rightmost_digits(my_int, my_digits):
    if my_digits is 1:
        return my_int

    my_str = str(my_int)
    return int(my_str[:-my_digits] + my_str[-my_digits + 1:] + my_str[-my_digits])

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

## lsBot corrections:
# make code more readable with variable names
# use == instead of 'is' for numbers

def rotate_string(num):
    return num[1:] + num[0]

def rotate_rightmost_digits(my_int, my_digits):
    my_str = str(my_int)
    fixed_part = my_str[:-my_digits]
    rest_of_digits = my_str[-my_digits:]

    return int(fixed_part + rotate_string(rest_of_digits))

'''PROBLEM 3: ROTATION PART 3
Take the number 735291 and rotate it by one digit to the left, getting 352917. Next, keep the first digit fixed in place and rotate the remaining digits to get 329175. Keep the first two digits fixed in place and rotate again to get 321759. Keep the first three digits fixed in place and rotate again to get 321597. Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579. The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer. You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

P
I = integer
O = max rotation integer
R
1. move first digit to the end
    735291 -> 352917 (rotate string function)
2. move 2nd to the end -> 329175
3. move 3rd to the end -> 321759
4. move 4th to the end -> 321597
5. move 5th to the end -> 321579 (6 numbers move 5)
E
-1 digit stays the same
D
integers and numeric strings
A
1. use len of string to calculate how many times we have to rotate the digits (range)
2. the range value is also use for the digits affected for the rotation
C'''

def rotate_string(num):
    return num[1:] + num[0]

def rotate_rightmost_digits(my_int, my_digits):
    my_str = str(my_int)
    fixed_part = my_str[:-my_digits]
    rest_of_digits = my_str[-my_digits:]

    return int(fixed_part + rotate_string(rest_of_digits))

def max_rotation(my_int):
    digit_rotate = my_int
    for idx in range(len(str(my_int)), 1, -1):
        digit_rotate = rotate_rightmost_digits(digit_rotate, idx)

    return digit_rotate

# simplified version of max_rotation function
# def max_rotation(my_int):
#     for idx in range(len(str(my_int)), 1, -1):
#         my_int = rotate_rightmost_digits(my_int, idx)

#     return my_int

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

'''PROBLEM 4: STACK MACHINE INTERPRETATION
-STACK -> list that grows(append) and pops (pop)
-STACK AND REGISTER, register s not part of the stack, can be tought as the current value
-MULT operation
    1. pops the topmost valye from slack
    2. mult pop value for current value in register
    3. replaces register content with result value

Write a function that implements a miniature stack and register based with the following operations:
P
I = strings arguments (tokens)
O = integer
R
- n, integer value in register
-PUSH, current value onto the stack
-ADD, pop value from stack and add to register
    (store result in register)
-SUB, pop value from stack and substract from register (update register)
-MULT, pop stack and multiply register
-DIV, pop stack and divide register by stack
    (store integer)
-REMAINDER, pop stack and div register by stack
    (store integer remainder)
-POP, remove topmost item from stack and place it in register
-PRINT register value

-program will use only string arguments and will not do anything like unknown tokens or empty arg

-stack starts as [] and register as 0
E
D
strings and lists
A
0. init stack = [] and register = 0
1. divide string in items with split
2. iterate created list
3. create different rules depending of the item list value
C'''

def minilang(my_string):
    stack = []
    register = 0

    actions = my_string.split()

    for item in actions:
        if item == 'PUSH':
            stack.append(register)

        elif item == 'ADD':
            register += stack.pop()

        elif item == 'SUB':
            register -= stack.pop()

        elif item == 'MULT':
            register *= stack.pop()

        elif item == 'DIV':
            register //= stack.pop()

        elif item == 'REMAINDER':
            register %= stack.pop()

        elif item == 'POP':
            register = stack.pop()

        elif item == 'PRINT':
            print(register)

        else:
            register = int(item)


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6
## this is the only one that doesnt make sense

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

## LS solution using match case

def minilang(program):
    stack = []
    register = 0

    for token in program.split():
        match token:
            case "ADD":
                register += stack.pop()
            case "DIV":
                register //= stack.pop()
            case "MULT":
                register *= stack.pop()
            case "REMAINDER":
                register %= stack.pop()
            case "SUB":
                register -= stack.pop()
            case "PUSH":
                stack.append(register)
            case "POP":
                register = stack.pop()
            case "PRINT":
                print(register)
            case _:
                register = int(token)

    return register

'''PROBLEM 5: WORD TO DIGIT
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.
P
I = string
O = string with digits
R
- numeric string converted to digit character
E
- words that are not numeric strings stay the same
D
list (store all numeric strings), strings, and integers
A
1. create list with numeric strings
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    create dict with dict comprehension 'zero': 0, ...
2. divide string into a list with split method
3. iterate through new list
    3.1 if string is in numeric_string_list
        replace dict key for value in new list
    3.2 else
        keep the same
4. join new list with join method

C'''

numeric_string_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

integer_dict = {item: idx for idx, item in enumerate(numeric_string_list)}

def word_to_digit(message):
    message_list = message.split()
    new_list = [str(integer_dict[word]) if word in numeric_string_list else word for word in message_list]

    return ' '.join(new_list)


message = 'Please call me at five five five one two three four'

print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# lsBot suggestions: create dictionary with all strings and simplify the list comprehension using method get with default value

numeric_string_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

integer_dict = {item: str(idx) for idx, item in enumerate(numeric_string_list)}

def word_to_digit(message):
    message_list = message.split()
    new_list = [integer_dict.get(word, word) for word in message_list]

    return ' '.join(new_list)

'''PROBLEM 6: IS IT PRIME
A prime number is a positive number that is evenly divisible only by itself and 1. Thus, 23 is prime since its only divisors are 1 and 23. However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24. Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument and returns True if the number is prime, False if it is not prime.

You may not use any of Python's add-on packages to solve this problem. Your task is to programmatically determine whether a number is prime without relying on functions that already do that for you.
P
I = positive integer
O = True if prime, False if not
R
-chek if integer is prime
E
D
list of integers
A
-how to check if number is divisible only by itself and 1?
-create a list of integers 2 to 9
-create var -> count
-iterate throug the list
    if num is equal to an integer in list skip
    if any of iterations of integer % my list has no remainder
        add 1 to counter
-if counter != 0 -> return False
-if not return True
C
'''

def is_prime(my_int):
    integers_list = [2, 3, 4, 5, 6, 7, 8, 9]

    if my_int == 1:
        return False

    count = 0
    for num in integers_list:
        if my_int % num == 0:
            count += 1

    if count != 0:
        return False

    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

# lsBot improvement:
# 1. keep loop iterating through divisors of number more open with a range adapting to the integer given
# 2. Simplify conditionals (remove count and return False directly if the modulo division is equal to zero)

def is_prime(my_int):
    if my_int == 1:
        return False

    for num in range(2, my_int):
        if my_int % num == 0:
            return False

    return True

## Launch school solution B, reducing options since the divisor of a number cannot be bigger than the square root

import math

def is_prime(number):
    if number == 1:
        return False

    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False

    return True

'''NUMBER 7: FIBONACCI NUMBERS(PROCEDURAL)
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)
I = integer (list of fibonacci)
O = integer (fibonacci number at that position)
R
-give the fibonacci number in the order number provided
E
D
integers
range
A
1. create first 2 fibonacci as 1 and 1
2. create an operation that takes last 2 fibonacci numbers and appends that number to the list
3. found the fibonacci in list created based on indexing
4. return that fibonacci number
C
'''

def fibonacci(my_idx):
    if my_idx == 1 or my_idx == 2:
        return 1

    fibonacci_list = [0, 1, 1]

    for fib_number in range(3, my_idx +1):
        fibonacci_list.append(fibonacci_list[fib_number - 1] + fibonacci_list[fib_number - 2])

    return fibonacci_list[my_idx]

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# first rectification, starting with first 2 digits 1 and 1

def fibonacci(my_idx):
    if my_idx == 1 or my_idx == 2:
        return 1

    fibonacci_list = [1, 1]

    for fib_number in range(2, my_idx):
        fibonacci_list.append(fibonacci_list[fib_number - 1] + fibonacci_list[fib_number - 2])

    return fibonacci_list[my_idx -1]

## LS solution, using to variables and only storing the last 2 values, that are the ones that will give us the current fibonacci number when we add them

def fibonacci(my_idx):
    if my_idx == 1 or my_idx == 2: # alternative if my_idx <= 2
        return 1

    prev, current = 1, 1

    for _ in range(2, my_idx):
        prev, current = current, prev + current

    return current

'''NUMBER 8: FIBONACCI NUMBERS (RECURSION)
recursion functions is functions that call itself
Recursive function has 3 primary qualities:
1. Must have a base case, simplest case (stop recursing the function)
2. Function calling itself when managing base case
3. Each recursive function is closer to the base than the current

Rewrite the fibonacci function using recursive functions
'''

# Example of recursive expression
# def sum_recursive(n):
#     if n == 1:
#         return 1

#     return n + sum_recursive(n - 1)

def fibonacci(n):
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

'''NUMBER 9: FIBONACCI NUMBERS (MEMOIZATION)
rewrite dictionary using memoization

Let's use dictionary to store the fibonacci numbers that occur already'''

fib_dict = {1: 1, 2: 1}

def fibonacci(n):
    if fib_dict.get(n):
        return fib_dict[n]

    fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_dict[n]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

## lsBot suggestions to improve code:
# 1. keep your code within the function, wrap up your recursive code within an inner function.
# 2. A better function that method get in this case is "in"

def fibonacci(n):
    fib_dict = {1: 1, 2: 1}

    def recursive_fib(n):
        if n in fib_dict:
            return fib_dict[n]

        fib_dict[n] = recursive_fib(n -1) + recursive_fib(n - 2)
        return fib_dict[n]

    return recursive_fib(n)

## Another example of memoized recursive function to calc sum of squares
dic_squares = {}

def sum_squares(n):
    if n == 1:
        return 1

    if n in dic_squares:
        return dic_squares[n]

    dic_squares[n] = n**2 + sum_squares(n - 1)
    return dic_squares[n]

'''PROBLEM 10: FIBONACCI
Write a function that calculates and returns the index of the first Fibonacci number that has the number of digits specified by the argument. The first Fibonacci number has an index of 1. You may assume that the argument is always an integer greater than or equal to 2.
I = integer (number of digits -> len num string)
O = integer (1st index number with that numb of digits)
R
E
D
list and variables
A
1. create a while loop
2. keep calling fibonacci function if len(str(fibonacci(n))) != digits
2. each new loop increase n by one
3. stop loop when len(str(fibonacci(n))) == digits
4. return n value
'''

import sys
sys.set_int_max_str_digits(50_000)

def fibonacci(n):
    fib_dict = {1: 1, 2: 1}

    def recursive_fib(n):
        if n in fib_dict:
            return fib_dict[n]

        fib_dict[n] = recursive_fib(n -1) + recursive_fib(n - 2)
        return fib_dict[n]

    return recursive_fib(n)

def find_fibonacci_index_by_length(digits):
    n = 1
    while len(str(fibonacci(n))) != digits:
        fibonacci(n)
        n += 1

    return n

All of these examples should print True
The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)

## lsBot correction, do not calculate all fibonacci numbers prior to the one we want to calculate

