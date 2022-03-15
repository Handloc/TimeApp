

import time


class Timer:
    def __init__(self, pomodoro_minutes=0, pomodoro_seconds=10, break_length=5, long_break_length=15):
        self.pomodoro_minutes = pomodoro_minutes
        self.pomodoro_seconds = pomodoro_seconds
        self.break_length = break_length
        self.long_break_length = long_break_length

    def time_printing(self):
        if self.pomodoro_minutes < 10 and self.pomodoro_seconds < 10:
            print(f'0{str(self.pomodoro_minutes)}:0{str(self.pomodoro_seconds)}')
        elif self.pomodoro_minutes < 10 and self.pomodoro_seconds >= 10:
            print(f'0{str(self.pomodoro_minutes)}:{str(self.pomodoro_seconds)}')
        elif self.pomodoro_minutes > 10 and self.pomodoro_seconds < 10:
            print(f'{str(self.pomodoro_minutes)}:0{str(self.pomodoro_seconds)}')
        else:
            print(f'{str(self.pomodoro_minutes)}:{str(self.pomodoro_seconds)}')

    def counting_down(self):
        if self.pomodoro_minutes >= 1 and self.pomodoro_seconds == 0:
            self.pomodoro_minutes -= 1
            self.pomodoro_seconds = 59
            while self.pomodoro_minutes >= 0 and self.pomodoro_seconds >= 0:
                while self.pomodoro_seconds >= 0:
                    if self.pomodoro_minutes >= 1 and self.pomodoro_seconds == 0:
                        self.time_printing()
                        self.pomodoro_minutes -= 1
                        self.pomodoro_seconds = 59
                    else:
                        self.time_printing()
                        time.sleep(0.01)
                        self.pomodoro_seconds -= 1
        elif self.pomodoro_minutes >= 1 and self.pomodoro_seconds >= 0:
            while self.pomodoro_seconds >= 0:
                self.time_printing()
                self.pomodoro_seconds -= 1
                if self.pomodoro_seconds == 0 and self.pomodoro_minutes >= 1:
                    self.time_printing()
                    self.pomodoro_minutes -= 1
                    self.pomodoro_seconds = 59
        else:
            while self.pomodoro_seconds >= 0:
                self.time_printing()
                self.pomodoro_seconds -= 1

        return "Time is up!!!"


new_pomodoro = Timer()
print(new_pomodoro.counting_down())
