from tkinter import *

root = Tk()
root.title('Life')

width1 = 500
height1 = 500


def main():
    pass


def ten():
    x = 10
    create(x)


def fifteen():
    x = 15
    create(x)


def twenty():
    x = 20
    create(x)


def restart():
    pass


def exit_game():
    root.destroy()


def save():
    pass

#Создает поле по выбранному значению
def create(x):
    pass


main_menu = Menu(root)
root.configure(menu=main_menu)

first = Menu(main_menu, tearoff=0)
second = Menu(main_menu, tearoff=0)
third = Menu(main_menu, tearoff=0)

first.add_cascade(label='Play', command=main)
first.add_cascade(label='New game', command=restart)
first.add_cascade(label='Exit', command=exit_game)

second.add_cascade(label='10 x 10', command=ten)
second.add_cascade(label='15 x 15', command=fifteen)
second.add_cascade(label='20 x 20', command=twenty)

third.add_cascade(label='Save', command=save)

main_menu.add_cascade(label='Life', menu=first)
main_menu.add_cascade(label='Size', menu=second)
main_menu.add_cascade(label='File', menu=third)

root.mainloop()