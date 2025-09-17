'''PROBLEM 1: LETTERCASE PERCENTAGE RATIO
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

P
I = string
O = dictionary with percentages
R
-percentage of lowercase
-percentage of uppercase
-percentage of non alpha char
-percentage value between '0.00' and '100.00'
-percentage values represented as strings and 2 decimals
E
-at least one char
-keys are always 'lowercase', 'uppercase', and 'neither'
D
string, lists to count number of items of each type, dictionary.
I
percentage might be a module of math, but it can do manually by comparing len of each substring to original string
    - f.e. 2/8 = 100 * count type / total -> percentage % do decimals
A
1. create dictionary with 3 constant keys and original values 0.00
2. iterate through char of string provided and create 2 lists
3. count len of both list and compare to len of string
4. create percentages, neither will be the difference
5. add values to dict and round decimals to 2
C'''

def letter_percentages(my_string):
    my_dict = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "0.00",
}
    lowercase_list = [char for char in my_string if char.islower()]
    uppercase_list = [char for char in my_string if char.isupper()]

    percentage_lower = 100 * len(lowercase_list) / len(my_string)
    percentage_upper = 100 * len(uppercase_list) / len(my_string)
    percentage_neither = 100 - percentage_lower - percentage_upper

    my_dict['lowercase'] = f"{percentage_lower:.2f}"
    my_dict['uppercase'] = f"{percentage_upper:.2f}"
    my_dict['neither'] = f"{percentage_neither:.2f}"

    return my_dict

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

## alternative solution using a unique for loop if/elif statements

def letter_percentages(my_string):

    count_lower = 0
    count_upper = 0
    count_other = 0

    for char in my_string:
        if char.islower():
            count_lower += 1

        elif char.isupper():
            count_upper += 1

        else:
            count_other += 1

    return {
        'lowercase': f"{100 * count_lower / len(my_string):.2f}",
        'uppercase': f"{100 * count_upper / len(my_string):.2f}",
        'neither': f"{100 * count_other / len(my_string):.2f}",
    }

'''PROBLEM 2. TRIANGLE SIDES
A triangle is classified as follows:

Equilateral: All three sides have the same length.
Isosceles: Two sides have the same length, while the third is different.
Scalene: All three sides have different lengths.
To be a valid triangle, the sum of the lengths of the two shortest sides must be greater than the length of the longest side, and every side must have a length greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the lengths of the three sides of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.


I = 3 numbers (integers or float) -> 3 sides of triangle
O = string from 4 options
R
-sum of 2 shortest sides > longer side
-len of each side > 0
- if either of 2 previous conditions are not met, triangle is not valid
- 3 sides equal -> Equilateral
- 2 sides equal and 1 different -> Isosceles
- 3 sides different -> Scalene
E
- no negative numbers
D
list of sides, (floats and integers) strings
A
1. create sides_list and sorted = [side1, side2, side3]
2. if condition -> if side 1 + side 2 < side 3 or 0 in [sides_list]
    return "invalid"
3. elif side1 == side2 == side3:
    return "Equilateral"
4. elif side1 != side2 and side1 != side3 and side2 != side3:
    return "Scalene"
5. else:
    Isosceles
C'''

def triangle(side1, side2, side3):
    list_sides = [side1, side2, side3]
    s1, s2, s3 = sorted(list_sides)

    if s1 + s2 <= s3 or s1 <= 0:
        return "invalid"

    elif s1 == s2 == s3:
        return "equilateral"

    elif s1 != s2 and s1 != s3 and s2 != s3:
        return "scalene"

    else:
        return "isosceles"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

## only correction I had to do is to check negative numbers even if it was not in the test cases

'''PROBLEM 3: TRI-ANGLES

A triangle is classified as follows:

Right: One angle is a right angle (exactly 90 degrees).
Acute: All three angles are less than 90 degrees.
Obtuse: One angle is greater than 90 degrees.
To be a valid triangle, the sum of the angles must be exactly 180 degrees, and every angle must be greater than 0. If either of these conditions is not satisfied, the triangle is invalid.

Write a function that takes the three angles of a triangle as arguments and returns one of the following four strings representing the triangle's classification: 'right', 'acute', 'obtuse', or 'invalid'.

You may assume that all angles have integer values, so you do not have to worry about floating point errors. You may also assume that the arguments are in degrees.

P
I = positive integer (degree format)
O = string from options ['right', 'acute', 'obtuse', 'invalid']
R
- valid triangle sum of angles == 180 and all angles must be greater than 0
- right: 1 angle is 90 degrees
- acute: 3 angles are less than 90 degrees
- obtuse: 1 angle is greater than 90 degrees
E
D
integers, list, sets (maybe), strings
A
1. create a list with angles and order using sorted
2. check if invalid triangle with if condition
    return "invalid"
3. check if a3 > 90
    return "obtuse"
4. check if 90 in list_angles:
    return "right"
5. else:
    return "acute"
C
'''

def triangle(ang1, ang2, ang3):
    list_angles = sorted([ang1, ang2, ang3])
    a1, a2, a3 = list_angles

    if sum(list_angles) != 180 or a1 <= 0:
        return "invalid"

    elif a3 > 90:
        return "obtuse"

    elif 90 in list_angles:
        return "right"

    else:
        return "acute"

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

'''PROBLEM 4: UNLUCKY DAYS

Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

P
I = integer (year above 1752)
O = integer (number of Fridays 13th)
R
-foresseable future calendar remains gregorian
E
D
integers, dates (year, month, and days)
A
0. Import date module
1. init count
2. loop through all months -> range(1, 13)
3. for each month use a date object to determine if 13th is a Friday
4. if so add 1 to count
4. return count
C
'''
import datetime

def friday_the_13ths(year):
    count_friday_13th = 0

    for month in range(1,13):
        if datetime.date(year, month, 13).weekday() == 4:
            count_friday_13th += 1

    return count_friday_13th

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

## LS solution

import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13)
                   for month in range(1, 13)]

    count = 0
    for day in thirteenths:
        if day.weekday() == 4:
            count += 1

    return count

'''PROBLEM 5: FEATURED NUMBER
I = integer
O = integer (next featured number)
R
feature number
    1. odd number
    2. multiple of 7
    3. unique digits
    4. <= 9876543201 -> if greater return "error" E

D
integers and strings
A
if start > 9876543201:
    return "error"

feature number in range (start + 1, 9876543202, 7)
    for number in range(feature):
        if number % 2 == 1 and len(set(number)) == len(number):
            return number C
'''

def next_featured(start):
    if start >= 9876543201:
        return "There is no possible number that fulfills those requirements."

    while True:
        start += 1
        if start % 7 == 0 and start % 2 == 1:
            break

    for number in range(start, 9876543202, 7):
        if number % 2 == 1 and len(set(str(number))) == len(str(number)):
            return number

print(next_featured(12))

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

## lsBot suggestions to improve code:
    # 1. create a step in the last loop to make sure all num are multiple of 7 and odd
    # 2. create helper functions for intermediate steps

def find_first_featured(number):
    while True:
        number += 1
        if number % 7 == 0 and number % 2 == 1:
            return number

def unique_digits(number):
    return len(set(str(number))) == len(str(number))

def next_featured(number):
    MAX_FEATURED = 9876543201

    featured_num = find_first_featured(number)

    while featured_num <= MAX_FEATURED:
        if unique_digits(featured_num):
            return featured_num

        featured_num += 14

    return "There is no possible number that fulfills those requirements."
    ## important to always return a value if the for loop doesn't find the num required

'''PROBLEM 6: SUM SQUARE - SQUARE SUM
Write a function that computes the difference between the square of the sum of the first count positive integers and the sum of the squares of the first count positive integers.
I = integer (count)
O = integer # 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
R
- count = 2 -> square of sum(num 1 + num2) - (num1 ** 2 + num2 ** 2)
E
- if count is 1 -> 0
D
range and integers
A
- create list with range(count)
- SUM SQUARE -> sum(list) ** 2
- SQUARE SUM -> sum[list comprehension ** 2]

return sum square - square sum

C
'''

def sum_square_difference(count):
    list_count = [num for num in range(1, count + 1)]

    square_of_sum = sum(list_count) ** 2
    sum_of_squares = sum(num ** 2 for num in list_count)

    return square_of_sum - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

## lsBot suggestion, solve the problem without using a list

def sum_square_difference(count):
    square_of_sum = sum(range(1, count + 1)) ** 2
    sum_of_squares = sum(num ** 2 for num in range(1, count + 1))

    return square_of_sum - sum_of_squares

'''PROBLEM 7: BUBBLE SORT

A bubble sort works by making multiple passes (iterations) through a list. On each pass, the two values of each pair of consecutive elements are compared. If the first value is greater than the second, the two elements are swapped. This process is repeated until a complete pass is made without performing any swaps. At that point, the list is completely sorted.

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least two elements.

6    2    7    1    4    Start: compare 6 > 2? Yes
2    6    7    1    4    Swap
2    6    7    1    4    6 > 7? No (no swap)
2    6    7    1    4    7 > 1? Yes
2    6    1    7    4    Swap
2    6    1    7    4    7 > 4? Yes
2    6    1    4    7    Swap

Write a function that takes a list as an argument and sorts that list using the bubble sort algorithm described above. The sorting should be done "in-place" -- that is, the function should mutate the list. You may assume that the list contains at least two elements.
P
I = list (min 2 items)
O = sorted list (in place - mutate)
R
- if 1st value greater than second -> swap
- if not (no swap)
- move from left to right
E
- works with integers and strings
based on the examples, the list keeps swaping until integers or names are ordered in increasing order -> default order of method .sort
D
list and mutation
A # [3, 2, 1] # 2 3 1 -> 2 1 3 -> 1 2 3

# help function -> mutate_list
    create count var
    if lst[idx] > lst[idx + 1]
        swaps items and add count

    if count != 0 return True

# main function
    - while list mutates keep calling mutate_list
        if list stops mutating:
            break
C
'''

def mutate_list(my_list):
    count = 0
    for idx in range(len(my_list) - 1):
        if my_list[idx] > my_list[idx + 1]:
            my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
            count += 1

    return count != 0

def bubble_sort(my_list):

    while True:
        if not mutate_list(my_list):
            break


lst1 = [3, 2, 1]
bubble_sort(lst1)
print(lst1)

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

## lsBot suggestion, use a flat instead of count in helper function

def mutate_list(my_list):
    swapped_in_pass = False ##line changed
    for idx in range(len(my_list) - 1):
        if my_list[idx] > my_list[idx + 1]:
            my_list[idx], my_list[idx + 1] = my_list[idx + 1], my_list[idx]
            swapped_in_pass = True ##line changed

    return swapped_in_pass ##line changed

def bubble_sort(my_list):

    while True:
        if not mutate_list(my_list):
            break