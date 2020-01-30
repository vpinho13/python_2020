#################################
# Vinicius Miranda de Pinho
# 30 jan 2020
# SQLITE3 basic class
#################################
#  import all libs and clear the terminal

import sqlite3
import os

# os.system('clear')

##################################
# sqlite3 database
##################################

# connect to database
conn = sqlite3.connect('database.db')
print("Path for this database is: database.db in the same project")

c = conn.cursor()

#####################################
# create a database table and if already exist, just skip
try:
    c.execute("""CREATE TABLE persons(
            first_name text,
            last_name text,
            email text) """)
except sqlite3.OperationalError:
    print("SQL DB already exit ")

emp1_first_name = ' Vinicius'
emp1_last_name = 'Pinho'
emp1_email = 'vinicius.pinho@elsys.com.br'

c.execute("INSERT INTO persons VALUES (:first_name,:last_name,:email)",
          {'first_name': emp1_first_name, 'last_name': emp1_last_name, 'email': emp1_email})

#  commit all database
conn.commit()

#  close the database connection
conn.close()
