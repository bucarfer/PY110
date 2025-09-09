'''PROBLEM 1: ASSESSMENT FORMAT
Our countdown to launch isn't behaving as expected. Why? Change the code so that our program successfully counts down from 10 to 1 before launching.'''

# OPT 1, adding keyword global and removing counter as an argument

def decrease():
    global counter
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    decrease()

print('LAUNCH!')

# OPT 2, reassigning counter inside the for loop

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

'''PROBLEM 2: REVERSE A STRING
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.'''

def reverse_string(string):
    for char in string:
        string = char + string

    return string

print(reverse_string("hello") == "olleh")

'''Solution: The problem is our starting point is the existing string while we have to start with a new string to add the character in reverse'''

def reverse_string(string):
    new_string = ''
    for char in string:
        new_string = char + new_string

    return new_string

'''solution 2: using slicing'''

def reverse_string(string):
    return string[::-1]

'''PROBLEM 3: MULTIPLY LIST
You want to multiply all elements of a list by 2. However, the function is not returning the expected result. Explain the bug, and provide a solution.'''

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# solution: the problem was that we were not mutating the list, we need to reassign the value using indexing

def multiply_list(lst):
    for idx in range(len(lst)):
        lst[idx] *= 2

    return lst

# solution 2: create a new list using list comprehension

def multiply_list(lst):
    return [item * 2 for item in lst]

'''PROBLEM 4: KEY CHECK
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?'''

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# solution: if the key doesnt' exist it will raise a keyError, either we do a try/except block or we use get instead with a default value

def get_key_value(my_dict, key):
    return my_dict.get(key, 'key not found')

'''PROBLEM 5: CALENDAR EVENT CHECKER
We have a list of events and want to check whether a specific date is available (i.e., no events planned for that date). However, the function always returns the wrong value.'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

# The logic was reverse, if the date is in the dictionary we want to return false because the day is not available

def is_date_available(date):
    if date in events:
        return False

    return True

# lsBot suggestion to make it more simple:

def is_date_available(date):
    return date not in events

'''PROBLEM 6: MUTABLE DEFAULT ARGUMENTS
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly: How would you fix this code?'''

def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

# solution: the problem was that the list is mutable and therefore was adding values from the previous function call, we can change the default parameter value to None and only create a new list if the user doesn't provide a list

def append_to_list(value, lst=None):
    if lst == None:
        lst = []
        lst.append(value)
        return lst

    else:
        lst.append(value)
        return lst

# more pythonic and idiomatic solution:

def append_to_list(value, lst=None):
    if lst is None: # better is None
        lst = []

    lst.append(value)
    return lst
    # separate the last 2 lines that are the same in both cases to avoid repetition

'''PROBLEM 7: SHADOW
We defined a function intending to multiply the sum of numbers by a factor. However, the function raises an error. Why? How would you fix this code?'''

def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)

# solution: the problem is that we are using a function name that shadows the summary built in function, we need to use a different name for our function

def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)

'''PROBLEM 8: COPY ISSUES
We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied list also seems to be affected:
What's wrong here? How can you fix it?'''

import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])

# solution: when we want to create an independent list from the original we need a deepcopy

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

'''PROBLEM 9: SET MODIFICATIONS
We want to remove certain items from a set while iterating over it, but the code below throws an error. Why is that and how can we fix it?'''

data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)

# the problem is that we are modifying a iterable list we can create a new collection instead of modifying the existing one

data_set = {1, 2, 3, 4, 5}
print({item for item in data_set if item % 2 == 1})

'''PROBLEM 10: LIST DEDUPLICATION
A developer is trying to remove duplicates from a list. They use a set for deduplication, but the order of elements is lost. How can we preserve the order?'''

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

## lsbot solution to separate new list from checking uniqueness

unique_data = []
seen = set()

for item in data:
    if item not in seen:
        seen.add(item)
        unique_data.append(item)