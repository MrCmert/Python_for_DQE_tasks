# import random int
from random import randint


# func for generate dict
def dict_generator(keys):
    # check if input is correct
    if not isinstance(keys, (str, list)):
        raise Exception("Wrong keys")
    elif isinstance(keys, list):
        keys = list(set(keys))

    if len(keys) == 0:
        raise Exception("No keys")

    new_dict = {}
    elements_in_dict = randint(1, len(keys))
    while len(new_dict) != elements_in_dict:
        # get random key
        key = keys[randint(0, len(keys) - 1)]
        # check if key already exist in dict
        if key in new_dict.keys():
            continue
        else:
            # set new key with random value
            new_dict[key] = randint(0, 100)
    return new_dict


# func for generate list of dicts
def list_of_dicts_generator(keys, quantity_of_dictionaries):
    list_of_dicts = []
    # fill list with dicts with random size and random key/value pair
    for i in range(quantity_of_dictionaries):
        new_dict = dict_generator(keys)
        list_of_dicts.append(new_dict)
    return list_of_dicts


# func for merging list of dicts
def merge_list(list_for_merge):
    # check if input is correct
    if not isinstance(list_for_merge, list):
        raise Exception("Wrong input")
    elif len(list_for_merge) == 0:
        raise Exception("Entered list is empty")
    elif not all(isinstance(x, dict) for x in list_for_merge):
        raise Exception("Entered list contain not only dicts")

    common_dict = {}
    already_inserted = []
    # adding key/value to common dict
    for i in range(len(list_for_merge)):
        # iterate by keys in dict
        for key in list_for_merge[i].keys():
            # check if key already inserted, skip it
            if key not in already_inserted:
                list_values = []
                # collect all values for this key
                for element in list_for_merge:
                    if key in element.keys():
                        list_values.append(element[key])
                # if value of key is max of list of all values for this key then insert to common dict
                if list_for_merge[i].get(key) == max(list_values):
                    # if key unique for all dicts, insert it as is
                    if len(list_values) == 1:
                        common_dict[key] = max(list_values)
                        already_inserted.append(key)
                    # if key not unique for all dicts, insert key with number of order of dict in list
                    elif len(list_values) > 1:
                        common_dict[key + "_" + str(i + 1)] = max(list_values)
                        already_inserted.append(key)
    return common_dict


# keys
letters_for_keys = "abcdefghijklmnopqrstuvwxyz"
# number of dicts
number_of_dicts = randint(2, 10)
new_list = list_of_dicts_generator(letters_for_keys, number_of_dicts)
print(new_list)
print(merge_list(new_list))

