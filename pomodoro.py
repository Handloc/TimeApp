from timer import TimerClass
from tkinter import *


class PomodoroClass(TimerClass):
    def __init__(self, parent):
        super().__init__(parent)
        self.break_finish = False
        self.all_cycles_are_finished = False
        self.cycle_counter = 1
        self.break_message = Label(self.parent, text='BREAK', font=('Arial', 35, 'bold'), bg='#494949', fg='green')
        self.pomodoro_finish_message = Label(self.parent, text='All pomodoro cycles\nare finished!',
                                             font=('Arial', 35, 'bold'), bg='#494949', fg='#db7a67')
        self.round_display = Label(self.parent, text='', font=('Arial', 35, 'bold'), bg='#494949', fg='#db7a67')
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.break_hours = 0
        self.break_minutes = 0
        self.break_seconds = 0
        self.num_of_cycles = 0

    def PomodoroCycle(self, hours=0, minutes=0, seconds=0, break_hours=0, break_minutes=0, break_seconds=0,
                      num_of_cycles=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.break_hours = break_hours
        self.break_minutes = break_minutes
        self.break_seconds = break_seconds
        self.num_of_cycles = num_of_cycles

    def PomodoroRound(self):
        self.timer_content.config(font=('Arial', 100), fg='#db7a67', bg='#494949', borderwidth=0)
        self.is_pomodoro = True
        if not self.pomodoro_finish and self.is_pomodoro:
            self.round_display.place(relx=0.5, rely=0.85, anchor=CENTER)
            self.round_display.config(text=f'{self.cycle_counter}/{self.num_of_cycles}')
            self.timer_start(self.hours, self.minutes, self.seconds)

    def BreakRound(self):
        self.is_break = True
        if not self.pomodoro_finish and self.is_break:
            self.timer_content.config(font=('Arial', 100), fg='green', bg='#494949', borderwidth=0)
            self.round_display.place(relx=0.5, rely=0.85, anchor=CENTER)
            self.round_display.config(text=f'{self.cycle_counter}/{self.num_of_cycles}')
            self.break_message.place(relx=0.5, rely=0.14, anchor=CENTER)
            self.timer_start(self.break_hours, self.break_minutes, self.break_seconds)
            self.cycle_counter += 1
            self.round_display.config(text=f'{self.cycle_counter}/{self.num_of_cycles}')
            if self.cycle_counter == self.num_of_cycles + 1:
                self.all_cycles_are_finished = True
                self.cycle_counter = 1
                self.round_display.place_forget()


