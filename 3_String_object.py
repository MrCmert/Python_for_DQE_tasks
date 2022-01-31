homework = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# just capitalize text
homework = homework.capitalize()
right_case = ''
for i in range(0, len(homework)):
    # upper case letter that after tab symbol or after dot
    if homework[i-1] == '\t' or homework[i-2:i] == '. ':
        right_case += homework[i].upper()
    else:
        right_case += homework[i]
print(right_case)

# replace wrong iz to is
final_result = right_case.replace(' iz ', ' is ')
print(final_result)

# count whitespaces
count_whitespaces = 0
for i in final_result:
    # check if character in list of whitespace characters
    if i in [' ', '\t', '\r', '\n', '\v', '\f']:
        count_whitespaces += 1
print("Number of whitespace characters: ", count_whitespaces)
