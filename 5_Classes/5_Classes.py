from datetime import datetime, timedelta


class Publication:
    def __init__(self, t="None"):
        self.text = t

    def publish(self):
        with open('news_feed.txt', 'a') as f:
            topic = str(type(self).__name__)
            new_topic = topic[0]
            for i in range(1, len(topic)):
                if topic[i] == topic[i].upper():
                    new_topic = new_topic + ' ' + topic[i]
                else:
                    new_topic = new_topic + topic[i]
            topic = new_topic
            minuses = 30 - len(topic)
            f.write(topic + ' ' + minuses * "-" + "\n")
            f.write(self.text)


class News(Publication):
    def __init__(self, t="None", c="None"):
        Publication.__init__(self, t=t)
        self.city = c

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write("\n" + self.city + ", " + str(datetime.strftime(datetime.today(), "%d/%m/%Y %H.%M")) + "\n\n")


class PrivateAd(Publication):
    def __init__(self, t="None", d=0):
        Publication.__init__(self, t=t)
        self.days = d
        self.exp_date = datetime.now() + timedelta(days=int(self.days))

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write("\nActual until: " + datetime.strftime(self.exp_date, "%d/%m/%Y") + ", "
                    + str(self.days) + " days left\n\n")


class BirthdayInThisMonth(Publication):
    def __init__(self, t="None", b=1, y=2020):
        Publication.__init__(self, t=t)
        self.birthday = b
        self.year = y

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(" birthday " +
                    str(datetime.strftime(datetime.today().replace(day=self.birthday, year=self.year), "%d %B."))
                    + "\nTurns " + str((datetime.now().year - self.year)) + " years old. Let's congratulate.\n\n")


if __name__ == "__main__":
    with open('news_feed.txt', 'w') as file:
        file.write("News feed:\n")

    record = True
    while record:
        n = input("Choose data type.\n"
                  "Enter - 1 if wanna add news.\n"
                  "Enter - 2 if wanna add privat ad\n"
                  "Enter - 3 if wanna add something\n"
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
            print("Time to see news feed today")
            record = False
