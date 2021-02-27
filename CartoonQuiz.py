from tkinter import *
import random
questions = [
    "What is the color of Dorami, Doraemon's sister?",
    "What is Gian's Passion?",
    "What does Doraemon makes scared?",
    "Who is Doraemon Best friend?",
    "What does Doraemon love to eat?",
    "What is the vegetable that Shinchan hates to eat?",
    "What is the color of the dress Shinchan's sister Himawari wears?",
    "Whom does Shinchan's teacher Yoshinaga marry?",
    "What is the name of Shinchan's favourite action hero?",
    "What is the name of Shinchan's mom?",

]

answer = [
    ["Pink", "Yellow", "Blue", "Black", ],
    ["Singing", "Dancing", "Irritating", "Studying", ],
    ["Gian", "Dorami", "Nobita's Mom", "Rat", ],
    ["Shizuka", "Gian", "Nobita", "Suneo", ],
    ["Chocolate", "Doracake", "Cookies", "None of the above", ],
    ["Garlic", "Beans", "Capsicum", "Carrot", ],
    ["Pink", "Yellow", "Blue", "Black", ],
    ["Kazama", "Suzuki", "Ishida Junichi", "Yamaha", ],
    ["Action Kamen", "Sailor Moon", "James Bond", "Captain Shinchan", ],
    ["Miranda", "Mandy", "Milli", "Misae", ],
]

ans = [1, 0, 3, 2, 1, 2, 1, 2, 1, 3]

user_answer = []

# generator function, taking random question and which are not repeatble
indexing = []


def gener():
    global indexing
    while(len(indexing) < 10):
        random_number = random.randint(0, 9)
        if random_number in indexing:
            continue
        else:
            indexing.append(random_number)
    print(indexing)

# calculating the score


def calc():
    global indexing, ans, user_answer
    x = 0
    score = 0
    for i in indexing:
        if user_answer[x] == ans[i]:
            score += 10
        x += 1
    print(score)
    showresult(score)

# Result showing


def showresult(score):
    labelQuestion.destroy()
    radiobutton1.destroy()
    radiobutton2.destroy()
    radiobutton3.destroy()
    radiobutton4.destroy()
    labelimg = Label(
        quiz_root,
        background="#ffffff"
    )
    labelimg.pack(pady=(25, 10))
    labelresult = Label(
        quiz_root,
        font=("Helvetica ", 20, 'bold'),
        background="#ffffff"

    )
    labelresult.pack()
    if score >= 70:
        img4 = PhotoImage(file="img6.png")
        labelimg.configure(image=img4)
        labelimg.image = img4
        labelresult.configure(text="You Are Awesome")
    else:
        img4 = PhotoImage(file="img5.png")
        labelimg.configure(image=img4)
        labelimg.image = img4
        labelresult.configure(text="You Lost The Game ")


# This function is responsible for selecting radio button, answer from user
ques = 1


def select():
    global radio, user_answer, labelQuestion, radiobutton1, radiobutton2, radiobutton2, radiobutton3, ques
    fetch = radio.get()
    user_answer.append(fetch)
    radio.set(-1)
    if ques < 10:
        labelQuestion.config(text=questions[indexing[ques]])
        radiobutton1['text'] = answer[indexing[ques]][0]
        radiobutton2['text'] = answer[indexing[ques]][1]
        radiobutton3['text'] = answer[indexing[ques]][2]
        radiobutton4['text'] = answer[indexing[ques]][3]
        ques += 1
    else:
        print(indexing)
        print(user_answer)
        calc()
# function section


def startquiz():
    global labelQuestion, radiobutton1, radiobutton2, radiobutton3, radiobutton4
    labelQuestion = Label(
        quiz_root,
        text=questions[indexing[0]],
        font='Helvetica 18 bold',
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"
    )
    labelQuestion.pack(pady=(50, 20))
    # selecting radio button

    global radio
    radio = IntVar()
    radio.set(-1)

    radiobutton1 = Radiobutton(
        quiz_root,
        text=answer[indexing[0]][0],
        font='Helvetica 13 bold',
        value=0,
        variable=radio,
        command=select,
        background="#ffffff"

    )
    radiobutton1.pack(side=TOP, ipady=5)

    radiobutton2 = Radiobutton(
        quiz_root,
        text=answer[indexing[0]][1],
        font='Helvetica 13 bold',
        value=1,
        variable=radio,
        command=select,
        background="#ffffff"
    )
    radiobutton2.pack(side=TOP, ipady=5)

    radiobutton3 = Radiobutton(
        quiz_root,
        text=answer[indexing[0]][2],
        font='Helvetica 13 bold',
        value=2,
        variable=radio,
        command=select,
        background="#ffffff"
    )
    radiobutton3.pack(pady=5)

    radiobutton4 = Radiobutton(
        quiz_root,
        text=answer[indexing[0]][3],
        font='Helvetica 13 bold',
        value=3,
        variable=radio,
        command=select,
        background="#ffffff"
    )
    radiobutton4.pack(pady=5)


def start():
    labelimg1.destroy()
    labelimg2.destroy()
    bottonstart.destroy()
    gener()
    startquiz()


quiz_root = Tk()

# width x height
quiz_root.geometry("500x400")

# width, height
quiz_root.minsize(200, 100)

# width, height
quiz_root.maxsize(1000, 700)

# title of thr GUI
quiz_root.title("CartoonQuiz")
# background color of window
quiz_root.configure(background="#ffffff")
# no resize using maxmize button of the window
quiz_root.resizable(0, 0)

# shinchan and doraemon image
img1 = PhotoImage(file="img1.png")
labelimg1 = Label(quiz_root, image=img1, background="#ffffff")
labelimg1.pack(pady=(40, 0))

# image for Cartoonquiz
img2 = PhotoImage(file="img2.png")
labelimg2 = Label(quiz_root, image=img2, background="#ffffff")
labelimg2.pack(pady=(0, 40))

# image for start button
img3 = PhotoImage(file="img3.png")
bottonstart = Button(quiz_root, image=img3,
                     background="#ffffff", relief=FLAT, command=start)
bottonstart.pack()

# for icon of window
# quiz_root.wm_iconbitmap("favicon.ico")

# frame of the window
#frame = Frame(quiz_root, borderwidth=2, bg="black", relief=RAISED)
# frame.pack(side=BOTTOM)

# botton creation
#bttn = Button(quiz_root, fg="black", text="Start")
# bttn.pack()


# close the wirndow
#Button(text="Close", command=quiz_root.destroy).pack()

quiz_root.mainloop()
