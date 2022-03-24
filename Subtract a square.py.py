'''
By ; youssef abdelghfar abdeltwab abdelghfar
name of game = Subtract a Square
'''


# to call tkinter library
from tkinter import *

# to call messagebox
from tkinter import messagebox

# number of coins
n_coins = 100


# number lock and unlock button for player one
def lock_buttons1():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)


def unlock_buttons1():
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
    b4.config(state=NORMAL)
    b5.config(state=NORMAL)
    b6.config(state=NORMAL)
    b7.config(state=NORMAL)


# number lock and unlock button for player two
def lock_buttons2():
    b11.config(state=DISABLED)
    b22.config(state=DISABLED)
    b33.config(state=DISABLED)
    b44.config(state=DISABLED)
    b55.config(state=DISABLED)
    b66.config(state=DISABLED)
    b77.config(state=DISABLED)


def unlock_buttons2():
    b11.config(state=NORMAL)
    b22.config(state=NORMAL)
    b33.config(state=NORMAL)
    b44.config(state=NORMAL)
    b55.config(state=NORMAL)
    b66.config(state=NORMAL)
    b77.config(state=NORMAL)

player12 = True

def subtract(button):
    global n_coins, player12
    if button["text"] == "1" and player12 == True:
        if n_coins - 1 < 0:
            messagebox.showinfo("no","canot")
        else:
            n_coins -= 1
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "2" and player12 == True:
        if n_coins - 4 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 4
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "3" and player12 == True:
        if n_coins - 9 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 9
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "4" and player12 == True:
        if n_coins - 16 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 16
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "5" and player12 == True:
        if n_coins - 25 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 25
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "6" and player12 == True:
        if n_coins - 36 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 36
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "7" and player12 == True:
        if n_coins - 49 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 49
            player12 = False
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons1()
            unlock_buttons2()
    elif button["text"] == "1" and player12 == False:
        if n_coins - 1 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 1
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "2" and player12 == False:
        if n_coins - 4 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 4
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "3" and player12 == False:
        if n_coins - 9 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 9
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "4" and player12 == False:
        if n_coins - 16 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 16
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "5" and player12 == False:
        if n_coins - 25 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 25
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "6" and player12 == False:
        if n_coins - 36 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 36
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()
    elif button["text"] == "7" and player12 == False:
        if n_coins - 49 < 0:
            messagebox.showinfo("no", "canot")
        else:
            n_coins -= 49
            player12 = True
            player_coins11.config(text=n_coins)
            player_coins22.config(text=n_coins)
            win()
            lock_buttons2()
            unlock_buttons1()


# Window size and title name
window = Tk()
window.geometry('800x500+460+160')
window.title('Subtract a square.')
window.resizable(False, False)

# frame for player one
fr1_pl1 = Frame(width='399', height='499', bg='green')
fr1_pl1.place(x=1, y=1)

# frame for player two
fr2_pl2 = Frame(width='399', height='499', bg='red')
fr2_pl2.place(x=393, y=1)

# name of player one
player_coins1 = Label(fr1_pl1, text='player 1 = ', fg='black', bg='white', font='arial 15')
player_coins1.place(x=-2, y=100)

# number of coins for player one
player_coins11 = Label(fr1_pl1, text=n_coins, fg='black', bg='white', font='arial 15')
player_coins11.place(x=90, y=100)

# name of player two
player_coins2 = Label(fr2_pl2, text='player 2 = ', fg='black', bg='white', font='arial 15')
player_coins2.place(x=-2, y=100)

# number of coins for player two
player_coins22 = Label(fr2_pl2, text=n_coins, fg='black', bg='white', font='arial 15')
player_coins22.place(x=90, y=100)

# Button for choice for player one
b1 = Button(fr1_pl1, text='1', fg='black', bg='white', font='arial 10', command=lambda: subtract(b1))
b1.place(x=120, y=250)
b2 = Button(fr1_pl1, text='2', fg='black', bg='white', font='arial 10', command=lambda: subtract(b2))
b2.place(x=140, y=250)
b3 = Button(fr1_pl1, text='3', fg='black', bg='white', font='arial 10', command=lambda: subtract(b3))
b3.place(x=160, y=250)
b4 = Button(fr1_pl1, text='4', fg='black', bg='white', font='arial 10', command=lambda: subtract(b4))
b4.place(x=180, y=250)
b5 = Button(fr1_pl1, text='5', fg='black', bg='white', font='arial 10', command=lambda: subtract(b5))
b5.place(x=200, y=250)
b6 = Button(fr1_pl1, text='6', fg='black', bg='white', font='arial 10', command=lambda: subtract(b6))
b6.place(x=220, y=250)
b7 = Button(fr1_pl1, text='7', fg='black', bg='white', font='arial 10', command=lambda: subtract(b7))
b7.place(x=240, y=250)

# Button for choice for player two
b11 = Button(fr2_pl2, text='1', fg='black', bg='white', font='arial 10', command=lambda: subtract(b11))
b11.place(x=120, y=250)
b22 = Button(fr2_pl2, text='2', fg='black', bg='white', font='arial 10', command=lambda: subtract(b22))
b22.place(x=140, y=250)
b33 = Button(fr2_pl2, text='3', fg='black', bg='white', font='arial 10', command=lambda: subtract(b33))
b33.place(x=160, y=250)
b44 = Button(fr2_pl2, text='4', fg='black', bg='white', font='arial 10', command=lambda: subtract(b44))
b44.place(x=180, y=250)
b55 = Button(fr2_pl2, text='5', fg='black', bg='white', font='arial 10', command=lambda: subtract(b55))
b55.place(x=200, y=250)
b66 = Button(fr2_pl2, text='6', fg='black', bg='white', font='arial 10', command=lambda: subtract(b66))
b66.place(x=220, y=250)
b77 = Button(fr2_pl2, text='7', fg='black', bg='white', font='arial 10', command=lambda: subtract(b77))
b77.place(x=240, y=250)
lock_buttons2()

# check who is winner
def win():
    if n_coins == 0 and player12 == False:
        messagebox.showinfo("Subtract a Square", "player one winner")
    elif n_coins == 0 and player12 == True:
        messagebox.showinfo("Subtract a Square", "player two winner")


window.mainloop()
