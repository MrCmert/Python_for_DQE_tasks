import re

homework = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

# count whitespaces using regexp
count_whitespaces = len(re.findall(r'\s', homework))
print("Number of whitespace characters: ", count_whitespaces)

# just capitalize text
homework = homework.capitalize()
right_case = ''
for i in range(0, len(homework)):
    # upper case letter that after tab symbol or after dot
    if homework[i - 1] == '\t' or homework[i - 2:i] == '. ':
        right_case += homework[i].upper()
    else:
        right_case += homework[i]
# delete empty lines
right_case = right_case.replace('\n\n', '\n')
print("Fix case letters and delete empty lines\n"+right_case)

# replace wrong iz to is
final_result = right_case.replace(' iz ', ' is ')
print("Text with correct is\n"+final_result)


# add sentence with last words
# find all last words
words_for_sentence = re.findall(r'[a-zA-Z0-9]*(?=\.)', final_result)
while '' in words_for_sentence:
    words_for_sentence.remove('')

# combine last words to sentence
result_sentence = " ".join(words_for_sentence) + '.'
result_sentence = result_sentence.capitalize()
print("Last word sentence\n"+result_sentence)

# add sentence in correct place
pattern = "add it to the END OF this Paragraph.".lower()
result_with_sentence = final_result.replace(pattern, pattern + ' ' + result_sentence)

print("Text with sentence\n"+result_with_sentence)

# add space before quoted word without space
quoted_without_space = re.findall(r'[^\s]([“].+?[”])', result_with_sentence)
for i in quoted_without_space:
    start_index = result_with_sentence.index(i)
    result_with_sentence = result_with_sentence[:start_index] + ' ' + result_with_sentence[start_index:]
print("Fix lack of space before quote\n"+result_with_sentence)

