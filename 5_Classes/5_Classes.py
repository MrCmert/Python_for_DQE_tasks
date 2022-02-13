from datetime import datetime, timedelta


class Publication:
    def __init__(self, t="None"):
        self.text = t

    def publish_topic(self):
        """
        :return: add name of class and text into file
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
            minuses = (30 - len(topic))*'-'
            f.write(f"{topic} {minuses}\n")

    def publish(self):
        with open('news_feed.txt', 'a') as f:
            f.write(self.text + "\n")


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


class PrivateAd(Publication):
    def __init__(self, t="None", d=0):
        Publication.__init__(self, t=t)
        self.days = d
        self.exp_date = datetime.now() + timedelta(days=int(self.days))
        self.insert_date = datetime.strftime(self.exp_date, "%d/%m/%Y")

    def publish(self):
        """
        :return: add topic, text, expiration date and days left  to file
        """
        Publication.publish_topic(self)
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(f"Actual until: {self.insert_date}, {self.days} days left\n\n")


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
                  "Enter - 0 if you ended add publications\n")
        if n == '1':
            text = input("Enter text of news: ")
            city = input("Enter city where it happened: ")
            n = News(text, city)
            n.publish()
        elif n == '2':
            text = input("Enter text of ad: ")
            days = int(input("Enter number of days it should be shown: "))
            a = PrivateAd(text, days)
            a.publish()
        elif n == '3':
            name = input("Enter name of the birthday boy: ")
            day = int(input("Enter day of birthday: "))
            year = int(input("Enter year of birthday: "))
            s = BirthdayInThisMonth(name, day, year)
            s.publish()
        elif n == '0':
            record = False
            print("Time to see news feed today")


if __name__ == "__main__":
    start_news()

