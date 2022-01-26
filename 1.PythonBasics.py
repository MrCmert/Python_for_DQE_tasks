import random # module for generate random int


# generate 100 random numbers and put it to list using list comprehensions
list = [random.randint(0, 1000) for i in range(0, 100)]

print(list)
# sort list from min to max (without using sort())
# using bubble sort
# iteration by all elements
for i in range(len(list)):
    # iteration by all elements except last and already sorted
    for j in range(0, len(list) - i - 1):
        # compare element with others
        if list[j] > list[j + 1]:
            # if this element more than another replace them. set max element in the end
            list[j], list[j+1] = list[j+1], list[j]

print(list)

sum_odd = 0
count_odd = 0
sum_even = 0
count_even = 0

# calculate sum and count of evens and odds
for i in list:
    if i % 2 == 0:
        sum_even = sum_even + i
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + i
        count_odd = count_even + 1

# exceptions if there are no even or odd numbers in the list
try:
    print("Avg even numbers: " + str(sum_even/count_even))
except ZeroDivisionError:
    print("Count even is " + str(count_even))

try:
    print("Avg odd numbers: " + str(sum_odd / count_odd))
except ZeroDivisionError:
    print("Count odd is " + str(count_odd))
