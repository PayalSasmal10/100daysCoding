import mysql.connector
from tkinter import *


def login_button():

    username = usernameEntry.get()
    password = passwordEntry.get()

    logindb(username, password)


def logindb(username, password):
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="root", db="bangaliyana")
    mycursor = db.cursor()

    try:
        mycursor.execute("DROP TABLE login_table")
        mycursor.execute(
            "CREATE TABLE login_table(fname VARCHAR(20), lname VARCHAR(20), birth DATE)")
        mycursor.execute(
            "INSERT INTO login_table(fname, lname, birth) VALUES('Payal', 'Sasmal', '1994-08-12')")
        db.commit()
        mycursor.execute("SELECT * from login_table")
        for i in mycursor:
            print(i)
    except:
        db.rollback()
        print("Error occured")


login_root = Tk()

login_root.geometry("400x300")
login_root.minsize(200, 100)
login_root.maxsize(400, 300)
login_root.resizable(0, 0)

labelUsername = Label(
    login_root,
    text="Username -",
    font=('Helvetica', 10, 'bold')
)
labelUsername.place(x=50, y=20)

usernameEntry = Entry(
    login_root,
    width=35,

)
usernameEntry.place(x=140, y=20, width=100)

labelPassword = Label(
    login_root,
    text="Password -",
    font=('Helvetica', 10, 'bold')
)
labelPassword.place(x=50, y=50)

passwordEntry = Entry(
    login_root,
    width=35,

)
passwordEntry.place(x=140, y=50, width=100)

loginbutton = Button(
    login_root,
    text="Login",
    command=login_button
)
loginbutton.place(x=140, y=90, width=100)

login_root.mainloop()
