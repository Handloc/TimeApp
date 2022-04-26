import time
from tkinter import *


class StopwatchClass:
    def __init__(self, parent):
        self.parent = parent
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.h = ''
        self.m = ''
        self.s = ''
        self.stop = False
        self.stopwatch_content = Label(self.parent, text='00:00:00')
        self.stopwatch_content.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.stopwatch_content.config(font=('Arial', 100), fg='#db7a67', bg='#494949', borderwidth=0)

    def stopwatch_start(self):
        while not self.stop:
            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
            if self.minutes == 60:
                self.hours += 1
                self.minutes = 0
            time.sleep(1)
            if self.hours < 10:
                self.h = f'0{self.hours}'
            elif self.hours >= 10:
                self.h = f'{self.hours}'
            if self.minutes < 10:
                self.m = f'0{self.minutes}'
            elif self.minutes >= 10:
                self.m = f'{self.minutes}'
            if self.seconds < 10:
                self.s = f'0{self.seconds}'
            elif self.seconds >= 10:
                self.s = f'{self.seconds}'
            self.stopwatch_content.config(text=f'{self.h}:{self.m}:{self.s}')
            self.stopwatch_content.update()

    def stopwatch_stop(self):
        self.stop = True

    def stopwatch_continue(self):
        self.stop = False
        self.stopwatch_start()

    def stopwatch_reset(self):
        self.stop = False
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.stopwatch_content.config(text=f'00:00:00')
        self.stopwatch_content.update()




