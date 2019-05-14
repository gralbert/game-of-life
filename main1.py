from tkinter import *
from classes import Cell

root = Tk()
root.title('Game of Life')
root.geometry('500x500')


def play_help():
    global stop
    stop = False
    play()


def play():
    global stop
    if not stop:
        one_step()
        root.after(400, play)


def stopping():
    global stop
    stop = True


def one_step():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].neighbours = 0
            for i_ in range(i-1, i+2):
                for j_ in range(j-1, j+2):
                    try:
                        if grid[i_][j_].get_status() \
                                and (i_ != i or j_ != j):
                            grid[i][j].add_neighbour()
                    except IndexError:
                        pass
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j].get_neighbours() == 3 \
                    and not grid[i][j].get_status():
                grid[i][j].change_color()

            elif (grid[i][j].get_neighbours() < 2
                  or grid[i][j].get_neighbours() > 3) \
                    and grid[i][j].get_status():
                grid[i][j].change_color()


def clear():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].clear()


def remake(sizex, sizey):
    global root
    root.geometry('{}x{}'.format(sizex*20,sizey*20 + 20))
    global grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].destroy()
    grid = create_grid(sizex, sizey)
    create_menu()
    global stop
    stop = False


def ten():
    remake(10,10)


def fifteen():
    remake(15, 15)


def twenty():
    remake(25, 25)


def exit_game():
    root.destroy()


def create_grid(sizex, sizey):
    y = -20

    grid = [[] * sizex for i in range(sizey)]
    for i in range(int(sizex)):
        x = -20
        y += 20
        for j in range(int(sizey)):
            x += 20
            grid[i].append(Cell())
            grid[i][j].place(x=x, y=y)

    return grid


def create_menu():
    main_menu = Menu(root)
    root.configure(menu=main_menu)
    file = Menu(main_menu, tearoff=0)
    run = Menu(main_menu, tearoff=0)
    size = Menu(main_menu, tearoff=0)

    file.add_cascade(label='Import', command=upload)
    file.add_cascade(label='Export', command=save)
    file.add_cascade(label='Exit', command=exit_game)

    run.add_cascade(label='Run', command=play_help)
    run.add_cascade(label='Stop', command=stopping)
    run.add_cascade(label='One step', command=one_step)
    run.add_cascade(label='Clear', command=clear)

    size.add_cascade(label='10 x 10', command=ten)
    size.add_cascade(label='15 x 15', command=fifteen)
    size.add_cascade(label='25 x 25', command=twenty)

    main_menu.add_cascade(label='File', menu=file)
    main_menu.add_cascade(label='Run', menu=run)
    main_menu.add_cascade(label='Size', menu=size)


if __name__ == '__main__':
    create_menu()
    stop = False
    grid = create_grid(25, 25)
    root.mainloop()
