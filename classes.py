import tkinter as tk


class Cell(tk.Label):
    def __init__(self):
        tk.Label.__init__(self, width=2,
                          height=1, fg='#eee',
                          bg="#eee", borderwidth=2,
                          relief="solid", font='Arial 10')
        self.status = False
        self.bind('<Button-1>', self.help_change_color)
        self.neighbours = 0

    def change_color(self):
        if self.status:
            self.configure(self, bg='#eee')
            self.status = False
        else:
            self.configure(self, bg='lightgreen')
            self.status = True

    def help_change_color(self, event):
        self.change_color()

    def get_status(self):
        return self.status

    def get_neighbours(self):
        return self.neighbours

    def add_neighbour(self):
        self.neighbours += 1

    def clear_neighbour(self):
        self.neighbours -= 1

    def clear(self):
        self.neighbours = 0
        self.status = False
        self.configure(self, bg='#eee')
