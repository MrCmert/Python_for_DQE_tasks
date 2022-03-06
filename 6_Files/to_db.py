import pyodbc


class ToDb:
    def __init__(self):
        self.connection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Database=publication.db")
        self.cursor = self.connection.cursor()
        # create tables if not exists
        self.cursor.execute("CREATE TABLE IF NOT EXISTS news ("
                            "text TEXT,"
                            "city TEXT"
                            ");")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS private_ad ("
                            "text TEXT,"
                            "date TEXT"
                            ");")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS birthday_in_this_month ("
                            "name TEXT,"
                            "day INTEGER,"
                            "year INTEGER"
                            ");")

    def insert_record(self, class_name, **kwargs):
        # get string of columns to insert
        column_names = []
        for i in kwargs.keys():
            column_names.append(i)
        columns = ', '.join(column_names)

        # get string of values to insert
        values = []
        for j in column_names:
            # if type(kwargs[j]) == int:
            #     values.append(f"{kwargs[j]}")
            # else:
            values.append(f"'{kwargs[j]}'")
        values_string = ', '.join(values)

        # get string to check
        elements = []
        for k in column_names:
            # if type(kwargs[j]) == int:
            #     elements.append(f"{k} = {kwargs[k]}")
            # else:
            elements.append(f"{k} = '{kwargs[k]}'")
        elements_string = " AND ".join(elements)
        self.cursor.execute(f"SELECT * FROM {class_name} "
                            f"WHERE {elements_string};")
        # check if value in db and insert
        m = self.cursor.fetchall()
        if len(m) == 0:
            self.cursor.execute(f"INSERT INTO {class_name} ({columns}) "
                                f"VALUES({values_string});")
            self.cursor.commit()
            print("Record inserted")
        else:
            print("Record already exists in db")
            return 0

    def __del__(self):
        self.cursor.commit()
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    # check what inserted to db
    connection = pyodbc.connect("Driver={SQLite3 ODBC Driver};Database=publication.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM news")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM private_ad")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM birthday_in_this_month")
    print(cursor.fetchall())
