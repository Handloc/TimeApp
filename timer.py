import time
from tkinter import *


class TimerClass:
    def __init__(self, parent):
        self.parent = parent
        self.h = ''
        self.m = ''
        self.s = ''
        self.stop = False
        self.timer_finish = False
        self.pomodoro_finish = False
        self.is_pomodoro_finished = False
        self.is_break_finished = False
        self.timer_content = Label(self.parent, text='')
        self.timer_content.config(font=('Arial', 100), fg='#db7a67', bg='#494949', borderwidth=0)
        self.is_pomodoro = False
        self.is_break = False
        self.timer_finish_message = Label(self.parent, text='Time is up!',
                                          font=('Arial', 35, 'bold'), bg='#494949', fg='#db7a67')

    def timer_start(self, hours=0, minutes=0, seconds=0):
        self.timer_content.place(relx=0.5, rely=0.3, anchor=CENTER)
        if hours > 0 and minutes == 0 and seconds == 0:
            if hours < 10:
                time.sleep(1)
                self.timer_content.config(text=f'{self.h}:00:00')
            elif hours >= 10:
                time.sleep(1)
                self.timer_content.config(text=f'{self.h}:00:00')
            hours -= 1
            minutes = 59
            seconds = 60
        elif (hours > 0 or minutes > 0) and seconds == 0:
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
                if not self.is_pomodoro and not self.is_break:
                    self.timer_finish_message.place(relx=0.5, rely=0.3, anchor=CENTER)
                    self.timer_content.place_forget()
                    self.timer_finish = True
                    break
                elif self.is_pomodoro:
                    self.is_pomodoro_finished = True
                    self.is_break_finished = False
                    self.is_pomodoro = False
                    self.is_break = True
                    print(f'Pomodoro: {self.is_pomodoro_finished}')
                    break
                elif self.is_break:
                    self.is_break_finished = True
                    self.is_pomodoro_finished = False
                    self.is_pomodoro = True
                    self.is_break = False
                    print("break end")
                    break
            else:
                seconds -= 1
                if minutes > 0 and seconds == 0:
                    minutes -= 1
                    seconds = 59
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
                        self.m = f'{int(minutes)  + 1}'
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
        self.timer_content.place_forget()
        self.stop = False
