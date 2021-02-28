import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost", user="root", passwd="root", database="bangaliyana")

mycursor = mydatabase.cursor()


mycursor.execute("show tables")

for test_table in mycursor:
    mycursor.execute("DROP TABLE test_table")

mycursor.execute(
    "create table test_table(fname VARCHAR(20), lname VARCHAR(20), birth DATE)")


mycursor.execute(
    """INSERT INTO test_table(fname, lname, birth) VALUES('payal', 'sasmal', '1994-08-12')""")
mydatabase.commit()
mycursor.execute(
    """INSERT INTO test_table(fname, lname, birth) VALUES('Oli', 'sasmal', '1994-12-12')""")
mydatabase.commit()


mycursor.execute("select * from test_table")
for i in mycursor:
    print(i)
