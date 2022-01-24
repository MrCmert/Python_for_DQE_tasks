# Python_for_DQE_tasks
#Create a python script:

#create list of 100 random numbers from 0 to 1000
#calculate average for even and odd numbers
#print both average result in console
#Each line of code should be commented with description.

#Commit script to git repository and provide link as home task result.
import random #module for generate random int

list = [] #create empthy list

#generate 100 random numbers and put it to list
for i in range(0, 100):
    list.append(random.randint(0, 1000))

#sort list from min to max (without using sort())
'''sorted_list = []
for i in list:
    if len(sorted_list) == 0:
        sorted_list.append(i)
    else:
        for j in range(0, len(sorted_list)):
            if i < sorted_list[j]:
                sorted_list.insert(j, i)'''

sum_odd = 0
count_odd = 0
sum_even = 0
count_even = 0

for i in list:
    if i % 2 == 0:
        sum_even = sum_even + i
        count_even = count_even + 1
    else:
        sum_odd = sum_odd + i
        count_odd = count_even + 1

print("Avg even: " + str(sum_even/count_even))
print("Avg odd: " + str(sum_odd/count_odd))


print(list)
#print(sorted_list)