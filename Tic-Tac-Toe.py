from tkinter import *
from tkinter import messagebox
import os

# functions are written here
i = True


def check(btn):
    global i
    if btn['text'] == '':
        if(i):
            i = False
            btn['text'] = 'X'
            result()
        else:
            i = True
            btn['text'] = 'O'
            result()


def result():
    if (btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X'):
        btn1.configure(bg='#ff6600')
        btn2.configure(bg='#ff6600')
        btn3.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X'):
        btn1.configure(bg='#ff6600')
        btn4.configure(bg='#ff6600')
        btn7.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X'):
        btn1.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X'):
        btn2.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn8.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X'):
        btn3.configure(bg='#ff6600')
        btn6.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'):
        btn3.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn7.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X'):
        btn4.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn6.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()
    elif(btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X'):
        btn7.configure(bg='#ff6600')
        btn8.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "X is winner")
        reset()

    # Logic for o player
    elif(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O'):
        btn1.configure(bg='#ff6600')
        btn2.configure(bg='#ff6600')
        btn3.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O'):
        btn1.configure(bg='#ff6600')
        btn4.configure(bg='#ff6600')
        btn7.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O'):
        btn1.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O'):
        btn2.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn8.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O'):
        btn3.configure(bg='#ff6600')
        btn6.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'):
        btn3.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn7.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()

    elif(btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O'):
        btn4.configure(bg='#ff6600')
        btn5.configure(bg='#ff6600')
        btn6.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()
    elif(btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O'):
        btn7.configure(bg='#ff6600')
        btn8.configure(bg='#ff6600')
        btn9.configure(bg='#ff6600')
        messagebox.showinfo("Result", "O is winner")
        reset()

    # logic for none of them are winner
    elif (btn1['text'] != '' and btn2['text'] != '' and btn3['text'] != '' and btn4['text'] != '' and btn5['text'] != ''
          and btn6['text'] != '' and btn7['text'] != '' and btn8['text'] != '' and btn9['text'] != ''):
        messagebox.showinfo("Result", "None of them are winners")
        reset()


def reset():
    btn1['text'] = ''
    btn2['text'] = ''
    btn3['text'] = ''
    btn4['text'] = ''
    btn5['text'] = ''
    btn6['text'] = ''
    btn7['text'] = ''
    btn8['text'] = ''
    btn9['text'] = ''

    btn1.configure(bg='#00A3A3')
    btn2.configure(bg='#00A3A3')
    btn3.configure(bg='#00A3A3')
    btn4.configure(bg='#00A3A3')
    btn5.configure(bg='#00A3A3')
    btn6.configure(bg='#00A3A3')
    btn7.configure(bg='#00A3A3')
    btn8.configure(bg='#00A3A3')
    btn9.configure(bg='#00A3A3')


tic_tac_toe_root = Tk()

tic_tac_toe_root.geometry("410x348+480+130")
tic_tac_toe_root.resizable(0, 0)
tic_tac_toe_root.maxsize(410, 348)
tic_tac_toe_root.minsize(410, 348)
tic_tac_toe_root.title("Tic-Tac-Toe By Payal")
tic_tac_toe_root.iconbitmap(os.path.join(sys.path[0], "tic-tac-toe.ico"))
tic_tac_toe_root.configure(bg='#ff3399')
#frame = tic_tac_toe_root(tic_tac_toe_root, height=400, width=400)
#frame.place(x=0, y=0)

# Buttons for play
btn1 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn1))
btn1.grid(row=0, column=0)

btn2 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn2))
btn2.grid(row=0, column=1)

btn3 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn3))
btn3.grid(row=0, column=2)

btn4 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn4))
btn4.grid(row=1, column=0)

btn5 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn5))
btn5.grid(row=1, column=1)

btn6 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn6))
btn6.grid(row=1, column=2)

btn7 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn7))
btn7.grid(row=2, column=0)

btn8 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn8))
btn8.grid(row=2, column=1)

btn9 = Button(tic_tac_toe_root, text='', font=('times', 20, 'bold'),
              height=3, width=8, bg='#00A3A3', command=lambda: check(btn9))
btn9.grid(row=2, column=2)

# reset button
#img1 = PhotoImage(file="reset.png")
# reset_btn = Button(tic_tac_toe_root, text='RESET', font=('arial', 7, 'bold'), bg='#ff0000', height=2, width=5, command=reset)
#reset_btn.place(x=180, y=360)
tic_tac_toe_root.mainloop()
