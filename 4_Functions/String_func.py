import re


# func for counting whitespaces
def count_whitespaces(string):
    count = len(re.findall(r'\s', string))
    return count


# func for normalize text
def normalize_text(string):
    if not isinstance(string, str):
        raise Exception("Wrong input")
    string = string.capitalize()
    right_case = ''
    for i in range(0, len(string)):
        # upper case letter that after tab symbol or after dot
        if string[i - 1] == '\t' or string[i - 2:i] == '. ':
            right_case += string[i].upper()
        else:
            right_case += string[i]
    right_case = right_case.replace('\n\n', '\n')
    return right_case


# func for change wrong word
def change_wrong_word(string, wrong, right):
    if not isinstance(string, str) or not isinstance(wrong, str) or not isinstance(right, str):
        raise Exception("Wrong input")
    string = string.replace(' ' + wrong + ' ', ' ' + right + ' ')
    return string


# func for adding last word sentence
def adding_last_word_sentence(string, pattern):
    if not isinstance(string, str) or not isinstance(pattern, str):
        raise Exception("Wrong input")

    # find words before dots
    words_for_sentence = re.findall(r'[a-zA-Z0-9]*(?=\.)', string)
    while '' in words_for_sentence:
        words_for_sentence.remove('')

    # combine last words to sentence
    result_sentence = " ".join(words_for_sentence) + '.'
    result_sentence = result_sentence.capitalize()

    # add sentence in correct place
    pattern = pattern.lower()
    result_with_sentence = string.replace(pattern, pattern + ' ' + result_sentence)

    return result_with_sentence


# func for adding space before quotes if it not have
def fix_spaces_before_quotes(string):
    if not isinstance(string, str):
        raise Exception("Wrong input")
    quoted_without_space = re.findall(r'[^\s]([“].+?[”])', string)
    for i in quoted_without_space:
        start_index = string.index(i)
        string = string[:start_index] + ' ' + string[start_index:]
    return string


homework = '''homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

print("Number of whitespace characters: ", count_whitespaces(homework))
sentence = normalize_text(homework)
print("Text after normalize\n"+sentence)
sentence = change_wrong_word(sentence, 'iz', 'is')
print("Text after replacing wrong placed word\n"+sentence)
sentence = adding_last_word_sentence(sentence, "add it to the END OF this Paragraph.")
print("Text with last word sentence inserted in place\n", sentence)
sentence = fix_spaces_before_quotes(sentence)
print("Text with space before quotes\n"+sentence)

