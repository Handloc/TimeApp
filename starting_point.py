from tkinter import *


class StartingPoint:
    def __init__(self, parent):
        self.parent = parent
        self.h = ''
        self.m = ''
        self.s = ''
        self.timer_content = Label(self.parent, text='')

    def show(self, hours, minutes, seconds, display_type):
        if hours >= 10:
            self.h = f'{hours}'
        else:
            self.h = f'0{hours}'
        if minutes >= 10:
            self.m = f'{minutes}'
        else:
            self.m = f'0{minutes}'
        if seconds >= 10:
            self.s = f'{seconds}'
        else:
            self.s = f'0{seconds}'
        if display_type == "pomodoro":
            self.timer_content.config(font=('Arial', 100), fg='#db7a67', bg='#494949', borderwidth=0)
        elif display_type == "break":
            self.timer_content.config(font=('Arial', 100), fg='green', bg='#494949', borderwidth=0)
        self.timer_content.config(text=f'{self.h}:{self.m}:{self.s}')
        self.timer_content.place(relx=0.5, rely=0.3, anchor=CENTER)

    def hide(self):
        self.timer_content.place_forget()
