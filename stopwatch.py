import time
import os

was_timer_stopped = False


class StopwatchClass:
    def __init__(self):
        self.minutes = 0
        self.seconds = 0
        self.stop = False

    def stopwatch_start(self):
        while not self.stop:
            self.seconds += 1
            if self.seconds == 60:
                self.minutes += 1
                self.seconds = 0
            time.sleep(1)
            if self.minutes < 10 and self.seconds < 10:
                print(f'0{self.minutes}:0{self.seconds}')
            elif self.minutes < 10 and self.seconds >= 10:
                print(f'0{self.minutes}:{self.seconds}')
            elif self.minutes > 10 and self.seconds < 10:
                print(f'{self.minutes}:0{self.seconds}')
            else:
                print(f'{self.minutes}:{self.seconds}')

    def stopwatch_stop(self):
        self.stop = True

    def stopwatch_continue(self):
        self.stop = False
        self.stopwatch_start()

    def stopwatch_reset(self):
        self.stop = False
        self.minutes = 0
        self.seconds = 0
        print(f'00:00')
