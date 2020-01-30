"""
vinicius miranda de pinho

null

integer

real

text

blob

28 de jan 2020

add new line

"""

import sqlite3
import time
from datetime import datetime
from employee_001 import Employee


def write_sqlite3():
    # current date and time
    dateTimeObj = datetime.now()
    timestamp = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print("date =", timestamp)
    print(type(timestamp))

    conn = sqlite3.connect('employee.db')

    c = conn.cursor()  # for call commands
    try:

        c.execute("""CREATE TABLE employee(
                    first text,
                    last text,
                    pay integer,
                    date text
                        )""")

    except sqlite3.OperationalError:
        print("SQL DB already exit")

    emp1 = Employee('john', 'doe', 65000)
    emp2 = Employee('vini', 'pinho', 75000)
    date_rec = timestamp

    # c.execute("INSERT INTO employee VALUES ('{}', '{}', '{}', '{}')".format(first_name, last_name, pay, date_rec))
    c.execute("INSERT INTO employee VALUES (:first, :last, :pay, :date)",
              {'first': emp1.first_name, 'last': emp1.last_name, 'pay': emp1.pay, 'date': date_rec})

    conn.commit()  # must be commit

    conn.close()

    return


write_sqlite3()
print("Record end SQL")
