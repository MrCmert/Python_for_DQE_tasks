import re
import csv


def count_words():
    """
    :return: write to csv file words and count number of these words in news_feed.txt
    """
    with open("news_feed.txt") as f:
        data = f.read().lower()

    # find all words
    rgx = re.compile(r"(\w[\w']*\w|\w)")
    words = rgx.findall(data)
    set_words = set(words)

    with open("count_words.csv", "w") as f:
        writer = csv.writer(f, delimiter="-", lineterminator="\n")
        for i in set_words:
            if str(i).isdigit():
                continue
            writer.writerow([i, words.count(i)])


def letter_count():
    """
    :return: write to csv file letters and statistic of these letters in news_feed.txt
    """
    with open("news_feed.txt") as f:
        data = f.read()

    letters = []

    for i in data:
        if i.isalpha():
            letters.append(i)

    letters_set = set(list(map(lambda x: x.lower(), letters)))
    all_letters = len(letters)

    with open("letter_count.csv", "w") as f:
        headers = ["letter", "count_all", "count_uppercase", "percentage"]
        writer = csv.DictWriter(f, fieldnames=headers, lineterminator="\n")
        writer.writeheader()
        for i in letters_set:
            writer.writerow({"letter": i,
                             "count_all": letters.count(i)+letters.count(i.upper()),
                             "count_uppercase": letters.count(i.upper()),
                             "percentage": round((letters.count(i)+letters.count(i.upper()))/all_letters*100, 2)})


if __name__ == "__main__":
    count_words()
    letter_count()
