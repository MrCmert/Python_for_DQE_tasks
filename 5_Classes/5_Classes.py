# Create a tool, which will do user generated news feed:

# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format

# You need to implement:

# 1.News – text and city as input. Date is calculated during publishing.
# 2.Privat ad – text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.

# Each new record should be added to the end of file. Commit file in git for review.
from datetime import datetime, timedelta


class Publication:
    def __init__(self, t):
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
            f.write(self.text + "\n")


class News(Publication):
    def __init__(self, t="None", c="None"):
        Publication.__init__(self, t=t)
        self.city = c

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(self.city + ", " + str(datetime.strftime(datetime.today(), "%d/%m/%Y %H.%M")) + "\n")
            f.write("\n")


class PrivateAd(Publication):
    def __init__(self, t="None", d=0):
        Publication.__init__(self, t=t)
        self.days = d
        self.exp_date = datetime.now() + timedelta(days=int(self.days))

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write("Actual until: " + datetime.strftime(self.exp_date, "%d/%m/%Y") + ", " + self.days + " days left\n")
            f.write("\n")


class Something(Publication):
    def __init__(self, t="None", c="None"):
        Publication.__init__(self, t=t)
        self.city = c

    def publish(self):
        Publication.publish(self)
        with open('news_feed.txt', 'a') as f:
            f.write(self.city + ", " + str(datetime.strftime(datetime.today(), "%d/%m/%Y %H.%M")) + "\n")
            f.write("\n")


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
            days = input("Enter number of days it should be shown: ")
            a = PrivateAd(text, days)
            a.publish()
        elif n == '3':
            text = input("Enter text of smth: ")
            days = input("Enter smth: ")
            s = Something(text, days)
            s.publish()
        elif n == '0':
            record = False
