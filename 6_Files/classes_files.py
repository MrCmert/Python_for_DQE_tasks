from datetime import datetime
import re
import os
from functions.string_func import normalize_text
import count_functions


class Publication:
    def __init__(self, t="None"):
        self.text = t

    def publish_topic(self):
        """
        :return: add name of class into file
        """
        with open('news_feed.txt', 'a') as f:
            topic = str(type(self).__name__)
            new_topic = topic[0]
            for i in range(1, len(topic)):
                if topic[i] == topic[i].upper():
                    new_topic = new_topic + ' ' + topic[i]
                else:
                    new_topic = new_topic + topic[i]
            topic = new_topic
            minuses = (30 - len(topic)) * '-'
            f.write(f"{topic} {minuses}\n")

    def publish(self):
        """
        :return: add text into file
        """
        with open('news_feed.txt', 'a') as f:
            f.write(self.text + "\n")

    def set_text(self, t):
        self.text = t


class News(Publication):
    def __init__(self, t="None", c="None"):
        Publication.__init__(self, t=t)
        self.city = c
        self.publication_date = str(datetime.strftime(datetime.today(), "%d/%m/%Y %H.%M"))

    def publish(self):
        """
        :return: add topic, text and publication date to file
        """
        Publication.publish_topic(self)
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(f"{self.city}, {self.publication_date}\n\n")

    def set_city(self, c):
        self.city = c

    def param_write(self):
        """
        check if parameters write correct and public it
        :return:
        """
        while True:
            text = input("Enter text of news: ")
            if len(text.replace(" ", "")) <= 0:
                print("Your news is empty. Try again")
            else:
                break
        self.set_text(text)
        while True:
            city = input("Enter city where it happened: ")
            if len(city.replace(" ", "")) <= 0:
                print("Your city is empty. Try again")
            else:
                break
        self.set_city(city)
        self.publish()


class PrivateAd(Publication):
    def __init__(self, t="None", exp_date='12/12/2022'):
        Publication.__init__(self, t=t)
        self.exp_date = datetime.strptime(exp_date, "%d/%m/%Y")
        self.days = (self.exp_date - datetime.today()).days
        if self.days < 0:
            self.days = 0
        self.insert_date = datetime.strftime(self.exp_date, "%d/%m/%Y")

    def publish(self):
        """
        :return: add topic, text, expiration date and days left  to file
        """
        Publication.publish_topic(self)
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(f"Actual until: {self.insert_date}, {self.days} days left\n\n")

    def set_exp_date(self, exp_date):
        self.exp_date = datetime.strptime(exp_date, "%d/%m/%Y")
        self.days = (self.exp_date - datetime.today()).days
        if self.days < 0:
            self.days = 0
        self.insert_date = datetime.strftime(self.exp_date, "%d/%m/%Y")

    def param_write(self):
        """
        check if parameters write correct and public it
        :return:
        """
        while True:
            text = input("Enter text of ad: ")
            if len(text.replace(' ', '')) <= 0:
                print("Your ad is empty. Try again")
            else:
                break
        self.set_text(text)
        while True:
            try:
                exp_date = input("Enter date until it should be shown, in format dd/mm/YYYY. Example: 12/09/2022 ")
                self.set_exp_date(exp_date)
            except ValueError:
                print("Wrong format of date. Try again")
                continue
            else:
                break
        self.publish()


class BirthdayInThisMonth(Publication):
    def __init__(self, n="None", b=1, y=2020):
        self.name = n
        self.birthday = b
        self.year = y
        self.birthday_date = datetime.strftime(datetime.today().replace(day=self.birthday, year=self.year), "%d %B")
        self.years_old = datetime.now().year - self.year

    def publish(self):
        """
        :return: add topic and birthday boy with date and years to file
        """
        Publication.publish_topic(self)
        with open('news_feed.txt', 'a') as f:
            f.write(f"{self.name} birthday {self.birthday_date}\nTurns {self.years_old} years old. "
                    f"Let's congratulate.\n\n")

    def set_name(self, name):
        self.name = name

    def set_birthday(self, day, year):
        self.birthday = day
        self.year = year
        self.birthday_date = datetime.strftime(datetime.today().replace(day=self.birthday, year=self.year), "%d %B")
        self.years_old = datetime.now().year - self.year

    def param_write(self):
        """
        check if parameters write correct and public it
        :return:
        """
        while True:
            name = input("Enter name of the birthday: ")
            if len(name.replace(' ', '')) <= 0:
                print("Your name is empty. Try again")
            else:
                break
        self.set_name(name)
        while True:
            try:
                day = int(input("Enter day of birthday: "))
                year = int(input("Enter year of birthday: "))
                self.set_birthday(day, year)
                if datetime.today().replace(day=self.birthday, year=self.year) > datetime.today():
                    print("We cannot celebrate unborn")
                    continue
            except ValueError:
                print("Wrong day or year of birthday. Try again")
                continue
            else:
                break
        self.publish()


class FromFiles:
    """
    read file and write to news feed.
    data in file should be in next lines after name of type
    """

    def __init__(self, path=""):
        self.path = path

    def set_path(self, path):
        self.path = path

    def read_file(self):
        """
        :return: write to file found type of data and delete source if success
        """
        inserted_lines = []
        with open(self.path, 'r') as f:
            data = f.read().split('\n')
            for i in range(len(data)):
                try:
                    if re.sub(r'\s', '', data[i].lower()) == "news":
                        n = News(normalize_text(data[i + 1]), normalize_text(data[i + 2]))
                        n.publish()
                        inserted_lines.append(i)
                        inserted_lines.append(i+1)
                        inserted_lines.append(i+2)
                    elif re.sub(r'\s', '', data[i].lower()) == "privatead":
                        p = PrivateAd(normalize_text(data[i + 1]), data[i + 2])
                        p.publish()
                        inserted_lines.append(i)
                        inserted_lines.append(i + 1)
                        inserted_lines.append(i + 2)
                    elif re.sub(r'\s', '', data[i].lower()) == "birthdayinthismonth":
                        b = BirthdayInThisMonth(normalize_text(data[i + 1]), int(data[i + 2]), int(data[i + 3]))
                        b.publish()
                        inserted_lines.append(i)
                        inserted_lines.append(i + 1)
                        inserted_lines.append(i + 2)
                        inserted_lines.append(i + 3)
                except ValueError:
                    print(f"Something wrong with data in file. Numbers of strings: {i + 2}, {i + 3}")
                    continue
        inserted_lines = list(map(lambda x: x + 1, inserted_lines))
        not_inserted_lines = []
        for i in range(1, len(data)+1):
            if i not in inserted_lines:
                not_inserted_lines.append(i)
        if len(not_inserted_lines) > 0:
            print(f"Inserted lines: {inserted_lines}")
            print(f"Not inserted lines: {not_inserted_lines}")
        else:
            os.remove(self.path)
            print("All data inserted")

    def param_write(self):
        """
        check if path exists
        :return:
        """
        while True:
            path = input("Enter path to file or file name if in the same place: ")
            if len(path.replace(' ', '')) <= 0:
                print("Your path is empty. Try again")
            else:
                self.set_path(path)
                try:
                    self.read_file()
                except FileNotFoundError:
                    print("File not exist. Try again")
                    continue
                break


def start_news():
    """
    start fill news feed
    :return: write all news in file
    """
    with open('news_feed.txt', 'w') as file:
        file.write("News feed:\n")

    record = True
    while record:
        n = input("Choose data type.\n"
                  "Enter - 1 if wanna add news.\n"
                  "Enter - 2 if wanna add privat ad\n"
                  "Enter - 3 if wanna add birthday in this month\n"
                  "Enter - 4 if wanna load data from file\n"
                  "Enter - 0 if you ended add publications\n")
        if n == '1':
            k = News()
            k.param_write()
        elif n == '2':
            a = PrivateAd()
            a.param_write()
        elif n == '3':
            b = BirthdayInThisMonth()
            b.param_write()
        elif n == '4':
            f = FromFiles()
            f.param_write()
        elif n == '0':
            record = False
            print("Time to see news feed today")


if __name__ == "__main__":
    start_news()
