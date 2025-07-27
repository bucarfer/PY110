# In the Python REPL or a script, increment values of the remaining numbers in the numbers list by 1. Also, try this with an element that doesn't exist, such as numbers[4]

numbers = [1, 2, 3, 4]

for index in range(len(numbers)):
    numbers[index] += 1

print(numbers)