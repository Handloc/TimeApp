import time
from tkinter import *


class TimerClass:
    def __init__(self, parent):
        self.parent = parent
        self.h = ''
        self.m = ''
        self.s = ''
        self.stop = False
        self.timer_content = Label(self.parent, text='')
        # tc = bg='#494949', fg='#db7a67', font=('Arial', 15, 'bold')

    def timer_start(self, hours=0, minutes=0, seconds=0):
        self.timer_content.pack()
        if (hours > 0 or minutes > 0) and seconds == 0:
            if hours < 10 and minutes < 10:
                self.timer_content.config(text=f'0{hours}:0{minutes}:00')
            elif hours >= 10 and minutes < 10:
                self.timer_content.config(text=f'{hours}:0{minutes}:00')
            elif hours < 10 and minutes >= 10:
                self.timer_content.config(text=f'0{hours}:{minutes}:00')
            else:
                self.timer_content.config(text=f'{hours}:{minutes}:00')
            self.timer_content.update()
            seconds = 60
            minutes -= 1
        while not self.stop:
            if hours == 0 and minutes == 0 and seconds == 0:
                self.stop = True
                break
            else:
                seconds -= 1
                if minutes > 0 and seconds == 0:
                    minutes -= 1
                    seconds = 60
                elif hours > 0 and minutes == 0:
                    hours -= 1
                    minutes = 60
                time.sleep(1)
                if hours < 10:
                    self.h = f'0{hours}'
                elif hours >= 10:
                    self.h = f'{hours}'
                if minutes == 60:
                    if hours < 10:
                        self.h = f'0{int(hours) + 1}'
                    elif hours >= 10:
                        self.h = f'{int(hours) + 1}'
                    self.m = f'00'
                elif minutes < 10:
                    self.m = f'0{minutes}'
                elif minutes >= 10:
                    self.m = f'{minutes}'
                if seconds == 60:
                    if minutes < 10:
                        self.m = f'0{int(minutes) + 1}'
                    elif minutes >= 10:
                        self.m = f'{int(minutes) + 1}'
                    self.s = f'00'
                elif seconds < 10:
                    self.s = f'0{seconds}'
                elif seconds >= 10:
                    self.s = f'{seconds}'

                self.timer_content.config(text=f'{self.h}:{self.m}:{self.s}')
                self.timer_content.update()

    def timer_stop(self):
        self.stop = True

    def timer_continue(self):
        self.stop = False
        self.timer_start(int(self.h), int(self.m), int(self.s))

    def timer_reset(self):
        self.timer_content.pack_forget()
        self.stop = False
