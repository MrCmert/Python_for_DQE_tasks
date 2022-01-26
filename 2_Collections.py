#1. create a list of random number of dicts (from 2 to 10)

#dict's random numbers of keys should be letter,
#dict's values should be a number (0-100),
#example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
#2. get previously generated list of dicts and create one common dict:

#if dicts have same key, we will take max value, and rename key with dict number with max value
#if key is only in one dict - take it as is,
#example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
#Each line of code should be commented with description.

# module for generate random int
import random

# generate number of dicts
number_of_dicts = random.randint(2, 10)
# letters for keys
letters = 'abcdefghijklmnopqrstuvwxyz'
# empty list
list_of_dicts = []

# fill list with dicts with random size and random key/value pair
for i in range(number_of_dicts):
    new_dict = {}
    elements_in_dict = random.randint(2, 10)
    while len(new_dict) != elements_in_dict:
        key = letters[random.randint(0, len(letters)-1)]
        # check if key exist
        if key in new_dict.keys():
            continue
        else:
            new_dict[letters[random.randint(0, len(letters)-1)]] = random.randint(0,100)
    list_of_dicts.append(new_dict)

print(list_of_dicts)