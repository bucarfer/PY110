'''Select all the fruits from the dictionary with a help function'''

produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(my_dict):
    dict_selected_fruit = {}

    for key in my_dict:
        if my_dict[key] == 'Fruit':
            dict_selected_fruit[key] = 'Fruit'
    return dict_selected_fruit

print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }

'''mutate the original list and duplicate the value of each element'''

def double_numbers(my_list):
    for index in range(len(my_list)):
        my_list[index] *= 2

    return my_list

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [2, 8, 6, 14, 4, 12]

'''Transform the list doubling only the elements with odd index'''

def double_odd_numbers(my_list):
    doubled_list = []

    for index in range(len(my_list)):
        if index % 2 == 1:
            doubled_list.append(my_list[index] * 2)
        else:
            doubled_list.append(my_list[index])

    return doubled_list

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_numbers(my_numbers))  # [2, 4, 6, 14, 2, 6]

# not mutated
print(my_numbers)                      # [1, 4, 3, 7, 2, 6]

'''Try coding a function that lets you multiply all the list elements by a specific value returning a new list'''

def multiply(my_list, multiplicand):
    new_list = []

    for item in my_list:
        new_list.append(item * multiplicand)

    return new_list

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]