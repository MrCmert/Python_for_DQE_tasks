# module for generate random int
import random

# generate 100 random numbers and put it to list using list comprehensions
rand_list = [random.randint(0, 1000) for i in range(0, 100)]

print(rand_list)
# sort list from min to max (without using sort())
# using bubble sort
# iteration by all elements
for i in range(len(rand_list)):
    # iteration by all elements except last and already sorted
    for j in range(0, len(rand_list) - i - 1):
        # compare element with next
        if rand_list[j] > rand_list[j + 1]:
            # if this element more than next replace them. set max element in the end
            rand_list[j], rand_list[j+1] = rand_list[j+1], rand_list[j]

print(rand_list)

# create lists for odd and even
list_odd = []
list_even = []

# filter odds and evens to different lists
for i in rand_list:
    if i % 2 == 0:
        list_even.append(i)
    elif i % 2 != 0:
        list_odd.append(i)

# calculate avg evens and handling division by 0
try:
    avg_even = sum(list_even)/len(list_even)
except ZeroDivisionError:
    avg_even = 0

# calculate avg odds and handling division by 0
try:
    avg_odd = sum(list_odd) / len(list_odd)
except ZeroDivisionError:
    avg_odd = 0

# print avg
print("Avg even numbers: " + str(avg_even))
print("Avg odd numbers: " + str(avg_odd))
