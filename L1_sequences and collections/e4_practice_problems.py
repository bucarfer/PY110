'''PRACTICE PROBLEM 1
given the tuple below how would you count the occurrences of "banana"'''

fruits = ("apple", "banana", "cherry", "date", "banana")

# solution:
print(fruits.count('banana'))

# count returns the integer with the amount of times, but we have to print it

'''PRACTICE PROBLEM 2:
Given the following set, what is the set's length?
Answer it without running the code'''

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(len(numbers))

# the solution is 5 since sets do not count duplicate values twice.
numbers = {1, 2, 3, 4, 5}

'''PRACTICE PROBLEM 3:
GIVEN THESE TWO SETS, HOW WOULD YOU OBTAIN A SET THAT CONTAINS ALL THE UNIQUE VALUES FROM BOTH SETS'''

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}


# Solution:
# with the union of both sets,
c = a.union(b)
print(c)
## {1, 2, 3, 4, 5, 6}

'''PRACTICE PROBLEM 4:
Given the following code, what will be the output without running the code'''

names = ["Fred", "Barney", "Wilma", "Betty", "Pebbles", "Bambam"]
name_positions = {}
for index, name in enumerate(names):
    name_positions[name] = index
print(name_positions)

# Solution:
## {"Fred": 0, "Barney": 1, "Wilma": 2, "Betty": 3, "Pebbles": 4, "Bambam": 5}

'''PRACTICE PROBLEM 5:
Calculate the total age given the following dictionary'''

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# Solution:
print(sum(ages.values()))  # 6174
# usually we assign the return to a variable and then we print the variable

'''PRACTICE PROBLEM 6:
determine the min age from the above age dictionary'''

#solution:
print(min(ages.values())) ##10

'''PRACTICE PROBLEM 7:
What would the following code output? try to answer without running the code'''

words = ['ant', 'bear', 'cat']
selected_words = []
for word in words:
    if len(word) > 3:
        selected_words.append(word)

print(selected_words)

# Solution:
#  it adds to new dict only the string with more than 3 characters.
# ['bear']

'''PRACTICE PROBLEM 8:
Given the following string, create a dictionary that represents the frequency with which each letter occurs. The frequency count should be case-sensitive'''

statement = "The Flintstones Rock"

# solution:

statement_dict = {}

statement= ''.join(statement.split())
for char in statement:
    if char not in statement_dict:
        statement_dict[char] = 1
    else:
        statement_dict[char] += 1

print(statement_dict)
# {'T': 1, 'h': 1, 'e': 2, 'F': 1, 'l': 1, 'i': 1, 'n': 2, 't': 2, 's': 2, 'o': 2, 'R': 1, 'c': 1, 'k': 1}

# alternative solution:

statement = statement.replace(' ', '')

statement_dict = {}

for char in statement:
    statement_dict[char] = statement_dict.get(char, 0) + 1

print(statement_dict)

'''PRACTICE PROBLEM 9:
What is the return value of the list comprehension below?
Try to answer without running the code'''

[num for num in [1, 2, 3] if num > 1]
#[2, 3]

'''PRACTICE PROBLEM 10:
What does the following code print and why?'''

dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# solution:
# ('b': 'bear')

'''PRACTICE PROBLEM 11:
What does the following code return? Answer without running code'''

lst = [1, 2, 3, 4, 5]
lst[:2]

# Solution:
# [1, 2], It does not include the last iterable

'''PRACTICE PROBLEM 12:
What would be the other of the following code? Without running the code'''

frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# Solution:
# AttributeError: 'frozenset' object has no attribute 'add'