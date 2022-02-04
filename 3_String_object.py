import re

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

# add sentence with last words
# find all last words and add it to list
list_string = final_result.split('.')
words_for_sentence = []
for i in list_string:
    each_word = i.split()
    if len(each_word) != 0 and each_word[len(each_word)-1].isdigit() is False:
        words_for_sentence.append(each_word[len(each_word)-1])

# combine last words to sentence
result_sentence = " ".join(words_for_sentence) + '.'
result_sentence = result_sentence.capitalize()
print(result_sentence)

# add sentence in correct place
pattern = "add it to the END OF this Paragraph.".lower()
result_with_sentence = final_result.replace(pattern, pattern + ' ' + result_sentence)

print(result_with_sentence)

# add space before quoted word without space
quoted_without_excape = re.findall(r'[^\s]([“].+?[”])', result_with_sentence)
for i in set(quoted_without_excape):
   start_index = result_with_sentence.index(i)
   result_with_sentence = result_with_sentence[:start_index] + ' ' + result_with_sentence[start_index:]
print(result_with_sentence)
