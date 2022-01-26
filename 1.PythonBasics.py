import random #module for generate random int

list = [] #create empthy list

#generate 100 random numbers and put it to list
for i in range(0, 100):
    list.append(random.randint(0, 1000))

print(list)
#sort list from min to max (without using sort())
sorted_list = []
for i in range(0, len(list)):
    sorted_list.append(min(list))  #find min of list and append to new list
    list.pop(list.index(min(list)))  #delete min from old list

print(sorted_list)

sum_odd = 0
count_odd = 0
sum_even = 0
count_even = 0

#calculate sum and count of evens and odds
for i in sorted_list:
    if i % 2 == 0:
        sum_even = sum_even + i
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + i
        count_odd = count_even + 1

#exceptions if there are no even or odd numbers in the list
try:
    print("Avg even numbers: " + str(sum_even/count_even))
except ZeroDivisionError:
    print("Count even is " + str(count_even))

try:
    print("Avg odd numbers: " + str(sum_odd / count_odd))
except ZeroDivisionError:
    print("Count odd is " + str(count_odd))
