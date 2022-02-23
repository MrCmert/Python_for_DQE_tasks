import re
import csv


def count_words():
    with open("news_feed.txt") as f:
        data = f.read().lower()

    rgx = re.compile(r"(\w[\w']*\w|\w)")
    words = rgx.findall(data)
    set_words = set(words)

    with open("count_words.csv", "w") as f:
        writer = csv.writer(f, delimiter="-")
        for i in set_words:
            writer.writerow([i, words.count(i)])


if __name__ == "__main__":
    count_words()