import json
import os
import re
from datetime import datetime
import xml.etree.ElementTree as ET

from count_functions import letter_count, count_words
from functions.string_func import normalize_text
from to_db import ToDb


class Publication:
    def __init__(self, t="None"):
        self.text = t
        self.file_name = "news_feed.txt"

    def get_file_name(self):
        return self.file_name

    def publish_topic(self):
        """
        :return: add name of class into file
        """
        with open(self.file_name, 'a') as f:
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
        with open(self.file_name, 'a') as f:
            f.write(self.text + "\n")

    def set_text(self, t):
        if len(t.replace(' ', '')) > 0:
            self.text = t
        else:
            raise ValueError


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
        with open(self.file_name, 'a') as f:
            f.write(f"{self.city}, {self.publication_date}\n\n")
        t = ToDb()
        t.insert_record(class_name="news", text=f"{self.text}", city=f"{self.city}")

    def set_city(self, c):
        if len(c.replace(' ', '')) > 0:
            self.city = c
        else:
            raise ValueError

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
        with open(self.file_name, 'a') as f:
            f.write(f"Actual until: {self.insert_date}, {self.days} days left\n\n")
        t = ToDb()
        t.insert_record(class_name="private_ad", text=f"{self.text}", date=f"{self.exp_date}")

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
        Publication.__init__(self)
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
        with open(self.file_name, 'a') as f:
            f.write(f"{self.name} birthday {self.birthday_date}\nTurns {self.years_old} years old. "
                    f"Let's congratulate.\n\n")
        t = ToDb()
        t.insert_record(class_name="birthday_in_this_month",
                        name=f"{self.name}",
                        day=f"{self.birthday}",
                        year=f"{self.year}")

    def set_name(self, name):
        if len(name.replace(' ', '')) > 0:
            self.name = name
        else:
            raise ValueError

    def set_birthday(self, day, year):
        self.birthday = day
        self.year = year
        if datetime.today().replace(day=self.birthday, year=self.year) > datetime.today():
            raise ValueError
        else:
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
    data of object should be in next lines after name of type
    example:
    news
    something go wrong
    tokyo
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
                        n = News()
                        n.set_text(normalize_text(data[i + 1]))
                        n.set_city(normalize_text(data[i + 2]))
                        n.publish()
                        inserted_lines.extend([i, i+1, i+2])
                    elif re.sub(r'\s', '', data[i].lower()) == "privatead":
                        p = PrivateAd()
                        p.set_text(normalize_text(data[i + 1]))
                        p.set_exp_date(data[i + 2])
                        p.publish()
                        inserted_lines.extend([i, i+1, i+2])
                    elif re.sub(r'\s', '', data[i].lower()) == "birthdayinthismonth":
                        b = BirthdayInThisMonth()
                        b.set_name(normalize_text(data[i + 1]))
                        b.set_birthday(int(data[i + 2]), int(data[i + 3]))
                        b.publish()
                        inserted_lines.extend([i, i+1, i+2, i+3])
                except ValueError:
                    print(f"Something wrong with data in file. Error in one of the strings: {i + 2}..{i + 4}")
                    continue
                except IndexError:
                    print(f"Not enough data for publication. In strings after: {i + 1}")
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
                    print("Something wrong with file. Try again")
                    continue
                break


class FromJson(FromFiles):
    """
    example of data in file
    {
    "objects" :[
    {
      "type"  : "News",
      "text"  : "Something happen",
      "city"  : "Kyiv"
    },
    {
      "type"  : "Private Ad",
      "text"  : "Selling garage",
      "date"  : "25/03/2022"
    }
    ]
    }
    :return: write to file found type of data from json and delete source if success
    """
    def read_file(self):
        is_delete = True
        # check that file json format
        try:
            with open(self.path, "r") as f:
                a = json.load(f)
        except json.decoder.JSONDecodeError:
            print("It is not json file. Try again")
            return 0

        for i in a["objects"]:
            try:
                if re.sub(r'\s', '', i["type"].lower()) == "news":
                    n = News()
                    n.set_text(i["text"])
                    n.set_city(i["city"])
                    n.publish()
                elif re.sub(r'\s', '', i["type"].lower()) == "privatead":
                    p = PrivateAd()
                    p.set_text(i["text"])
                    p.set_exp_date(i["date"])
                    p.publish()
                elif re.sub(r'\s', '', i["type"].lower()) == "birthdayinthismonth":
                    b = BirthdayInThisMonth()
                    b.set_name(i["name"])
                    b.set_birthday(int(i["day"]), int(i["year"]))
                    b.publish()
            except (ValueError, KeyError):
                print(f"Something wrong with data of the file in this part {i}")
                is_delete = False
                continue

        if is_delete:
            os.remove(self.path)
            print("All data inserted")
        else:
            print("Something wrong with data in file")


class FromXml(FromFiles):
    """
    example of data in file:
    <Objects>
        <Element name="News">
            <Text>Something happen</Text>
            <City>Kyiv</City>
        </Element>
    </Objects>
        :return: write to file found type of data from xml and delete source if success
    """
    def read_file(self):
        is_delete = True

        try:
            tree = ET.parse(self.path)
        except ET.ParseError:
            print("It is not xml file. Try again")
            return 0

        root = tree.getroot()
        for element in root:
            try:
                if re.sub(r'\s', '', element.attrib["name"].lower()) == "news":
                    n = News()
                    n.set_text(element.find("Text").text)
                    n.set_city(element.find("City").text)
                    n.publish()
                elif re.sub(r'\s', '', element.attrib["name"].lower()) == "privatead":
                    p = PrivateAd()
                    p.set_text(element.find("Text").text)
                    p.set_exp_date(element.find("Date").text)
                    p.publish()
                elif re.sub(r'\s', '', element.attrib["name"].lower()) == "birthdayinthismonth":
                    b = BirthdayInThisMonth()
                    b.set_name(element.find("Name").text)
                    b.set_birthday(int(element.find("Day").text), int(element.find("Year").text))
                    b.publish()
            except (ValueError, AttributeError):
                print(f"Something wrong with data in element with index {list(root).index(element)}")
                is_delete = False
                continue

        if is_delete:
            os.remove(self.path)
            print("All data inserted")
        else:
            print("Something wrong with data in file")


def start_news():
    """
    start fill news feed
    :return: write all news in file
    """
    p = Publication()
    with open(p.get_file_name(), 'w') as file:
        file.write("News feed:\n")

    record = True
    while record:
        n = input("Choose data type.\n"
                  "Enter - 1 if wanna add news.\n"
                  "Enter - 2 if wanna add privat ad\n"
                  "Enter - 3 if wanna add birthday in this month\n"
                  "Enter - 4 if wanna load data from file\n"
                  "Enter - 5 if wanna load data from json file\n"
                  "Enter - 6 if wanna load data from xml file\n"
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
        elif n == '5':
            j = FromJson()
            j.param_write()
        elif n == '6':
            x = FromXml()
            x.param_write()
        elif n == '0':
            record = False
            print("Time to see news feed today")

        count_words(p.get_file_name())
        letter_count(p.get_file_name())


if __name__ == "__main__":
    start_news()
