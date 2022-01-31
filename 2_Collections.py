# import random int
from random import randint

# generate number of dicts
number_of_dicts = randint(2, 10)
# letters for keys
letters = 'abcdefghijklmnopqrstuvwxyz'
# empty list of dicts
list_of_dicts = []

# fill list with dicts with random size and random key/value pair
for i in range(number_of_dicts):
    new_dict = {}
    elements_in_dict = randint(1, len(letters))
    # fill dicts
    while len(new_dict) != elements_in_dict:
        # get random key
        key = letters[randint(0, len(letters)-1)]
        # check if key already exist in dict
        if key in new_dict.keys():
            continue
        else:
            # set new key with random value
            new_dict[key] = randint(0, 100)
    list_of_dicts.append(new_dict)

print(list_of_dicts)

common_dict = {}
already_inserted = []
# adding key/value to common dict
for i in range(len(list_of_dicts)):
    # iterate by keys in dict
    for key in list_of_dicts[i].keys():
        # check if key already inserted, skip it
        if key not in already_inserted:
            list_values = []
            # collect all values for this key
            for element in list_of_dicts:
                if key in element.keys():
                    list_values.append(element[key])
            # if value of key is max of list of all values for this key then insert to common dict
            if list_of_dicts[i].get(key) == max(list_values):
                # if key unique for all dicts, insert it as is
                if len(list_values) == 1:
                    common_dict[key] = max(list_values)
                    already_inserted.append(key)
                # if key not unique for all dicts, insert key with number of order of dict in list
                elif len(list_values) > 1:
                    common_dict[key + "_" + str(i+1)] = max(list_values)
                    already_inserted.append(key)

print(common_dict)


