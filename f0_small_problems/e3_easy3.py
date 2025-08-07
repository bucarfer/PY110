'''EXERCISE 1: After midnight (part1)
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.


P
I = takes integer (minutes)
O = item(hh:mm)
RULES
-minutes positive after midnight
-minutes negative before midnight
-minutes // 60 = hours
-minutes % 60 = minutes left
- minutes in one day 1440
with the examples we can see what happens if number of minutes is greater than 1440 (minutes in one day)
D
integers
A

1. if number is >1440 or <-1440
    remainder = modulo division %1440

    if minutes <0:
        minutes = minutes + 1440

    if minutes >0:
        hours = minutes // 60
        minutes = minutes % 60

    return string interpolation of hours and minutes with 2 digits

C'''

def time_of_day(minutes):
    if minutes > 1440 or minutes < -1440 :
        minutes = minutes % 1440

    if minutes < 0:
        minutes = minutes + 1440

    if minutes >= 0:
        hours = minutes // 60
        minutes = minutes % 60

    return f"{hours:02d}:{minutes:02d}"


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# do it using constant

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def time_of_day(my_minutes):
    total_minutes = my_minutes % MINUTES_PER_DAY

    hours = total_minutes // MINUTES_PER_HOUR
    minutes = total_minutes % MINUTES_PER_HOUR

    return f"{hours:02d}:{minutes:02d}"

'''EXERCISE 2: After Midnight (Part2)
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.
P
I = string with format (hh:mm)
O = minutes per day
RULES
E
inverse problem as previous one
D
strings and integers
A
1.take first 2 char -> pass to int and multiply by 60 to pass it to minutes
2. take last 2 char -> pass to int
3. return addition of previous minutes
C'''

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def after_midnight(my_string):
    if my_string == '24:00':
        return 0
    else:
        return (int(my_string[:2]) * MINUTES_PER_HOUR) + int(my_string[-2:])

def before_midnight(my_string):
    if my_string == '00:00' or my_string == '24:00':
        return 0
    else:
        return MINUTES_PER_DAY - after_midnight(my_string)

## lsBot using split ":"

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY

def after_midnight(my_string):
    hours, minutes = [int(item) for item in my_string.split(":")]
    return (hours * MINUTES_PER_HOUR + minutes) % MINUTES_PER_DAY

def before_midnight(my_string):
    total_minutes = MINUTES_PER_DAY - after_midnight(my_string)

    if total_minutes == MINUTES_PER_DAY:
        total_minutes = 0

    return total_minutes

'''EXERCISE 3: Double Char(Part1)
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
P
I = string
O = new string (every char double)
E
D
string
A
new string
for char in string
    new_string = 2 * char
return new_string

C
'''

def repeater(my_str):
    new_str = ''
    for char in my_str:
        new_str += char * 2
    return new_str

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")

## LSbot use list comprehension

def repeater(my_str):
    return ''.join([2 * char for char in my_str])

'''EXERCISE 4: Double Char(Part2)
P
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

I = string
O = new string
RULES
-double consonants
-not double vowels, digits, punctuation, or whitespace.
E
D
strings and lists
A
new string
def variable vowels = 'aeiou'
for loop over all char
    if char.isalpha() and char not in vowels:
        char * 2 in new string
    else:
        char in new string
return new_string
C
'''
def double_consonants(my_str):
    new_string = ''
    vowels = 'aeiou'
    for char in my_str:
        if char.isalpha() and char.lower() not in vowels:
            new_string += 2 * char
        else:
            new_string += char

    return new_string

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

## lsBot do it again using a list and .join

def double_consonants(my_str):
    new_string = []
    vowels = 'aeiou'

    for char in my_str:
        if char.isalpha() and char.lower() not in vowels:
            new_string.append(2 * char)
        else:
            new_string.append(char)

    return ''.join(new_string)

'''EXERCISE 5: reverse number
Write a function that takes a positive integer as an argument and returns that number with its digits reversed

P
I = positive integer
O = number with its digits reversed
RULES

E
D
integer integer
A
transform str apply sorted (reverse)
return transf int
C
'''

def reverse_number(num):
    reverse_str = str(num)[::-1]
    return int(reverse_str)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

## lsBot suggestion, combine both lines into 1

def reverse_number(num):
    return int(str(num)[::-1])

'''EXERCISE 6: Counting Up
Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

You may assume that the argument will always be a positive integer.

P
I = integer
O = list
RULES
returns a list containing all integers between 1 and the int arg (inclusive)
E
D
int and lists
A
def empty list
range(int + 1) -> loop
    apppend -> empty list
return list
C
'''

def sequence(my_int):
    empty_list = []

    for num in range(1, my_int + 1):
        empty_list.append(num)

    return empty_list


print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

## lsBot suggestion list comprehension

def sequence(my_int):
    return [num for num in range(1, my_int + 1)]

## LS solution

def sequence(my_int):
    return list(range(1, my_int + 1))

'''EXERCISE 7: Name Swapping
Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").
P
I = str -> name surname
O = str -> surname, name
RULES
E
D
strings + lists
A
list = split the string with .split() method -> reverse list
new_str = join the list with connector ", "
return new_str
C
'''

def swap_name(my_str):
    my_list = (my_str.split())[::-1]
    new_str = ", ".join(my_list)
    return new_str

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

## lsBot solution

def swap_name(name):
    return ', '.join(name.split()[::-1])

## do the further exploration problem

def swap_name(my_str):
    my_list = (my_str.rsplit(' ', 1))[::-1]
    new_str = ", ".join(my_list)
    return new_str

'''EXERCISE 8: Sequence count

'''