import tkinter
from tkinter import *
from tkinter import ttk
import stopwatch, pomodoro, timer
import threading

root = Tk()
root.title('TimeApp')
style = ttk.Style()

# Creating a thread to run timer function in background
# def stopwatch_threading(func):
#     stopwatch_th = threading.Thread(target=func)
#     stopwatch_th.start()


style.theme_create('Tab-style', parent="classic", settings={
    ".": {
        "configure": {
            "background": '#494949',  # Background color
            "font": "white"
        }
    },
    "TNotebook": {
        "configure": {
            "background": '#212121',  # Background color next to tabs
            "tabmargins": [5, 5, 0, 0],  # Margins: left, top, right, between tab and frames
            "borderwidth": 0
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": '#2b2b2b',  # Non-selected tab background
            "padding": [5, 2],
            "borderwidth": 1
        },
        "map": {
            "foreground": [("selected", "black"), ("!disabled", "#f8f8ff")],  # Font color
            "background": [("selected", '#db7a67')],  # Selected tab background
            "expand": [("selected", [1, 1, 1, 0])],  # Expanse of text
            "highlightbackground": "red"
        }
    }
})

style.theme_use("Tab-style")
menu = ttk.Notebook(root, width=900, height=600)

# TIMER ----------------------------------------------------------------------------------------------------------------
timer_tab = ttk.Frame(menu)
menu.add(timer_tab, text='Timer')
timer_content = Label(timer_tab, text='TIMER', font=('Ink Free', 30, 'bold'), bg='#494949', fg='#db7a67')
timer_content.pack()

hour = Entry(timer_tab)
hour.place(height=100, width=78, x=348, y=100, anchor=CENTER)
hour.config(font=('Arial', 50, 'bold'), fg='#db7a67')

spacing_mark = Label(timer_tab, text=':', bg='#494949', fg='#db7a67', font=('Arial', 50, 'bold'))
spacing_mark.place(x=400, y=100, anchor=CENTER)

minute = Entry(timer_tab)
minute.place(height=100, width=78, relx=0.5, y=100, anchor=CENTER)
minute.config(font=('Arial', 50, 'bold'), fg='#db7a67')

second = Entry(timer_tab)
second.place(height=100, width=78)
second.config(font=('Arial', 50, 'bold'), fg='#db7a67')


def validation():
    if int(minute.get()) <= 60 and int(second.get()) <= 60:
        starting_point.show(int(hour.get()),
                            int(minute.get()),
                            int(second.get()))
        timer_start_button.pack(pady=15)
        error_message.pack_forget()
        timer_ok_button.pack_forget(),
        hour.pack_forget(),
        minute.pack_forget(),
        second.pack_forget(),
    elif int(minute.get()) > 60 and int(second.get()) > 60:
        error_message.config(text='Value of minutes and seconds cannot be grater than 60',
                             bg='#494949',
                             fg='red',
                             font=('Arial', 14))
        error_message.pack()

    elif int(minute.get()) > 60 and int(second.get()) <= 60:
        error_message.config(text='Value of minutes cannot be greater than 60',
                             bg='#494949',
                             fg='red',
                             font=('Arial', 14))
        error_message.pack()

    elif int(minute.get()) <= 60 and int(second.get()) > 60:
        error_message.config(text='Value of seconds cannot be greater than 60',
                             bg='#494949',
                             fg='red',
                             font=('Arial', 14))
        error_message.pack()


timer_counter = timer.TimerClass(timer_tab)


class StartingPoint:
    def __init__(self):
        self.h = ''
        self.m = ''
        self.s = ''
        self.stopwatch_content = Label(timer_tab, text=f'')

    def show(self, hours, minutes, seconds):
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
        self.stopwatch_content.config(text=f'{self.h}:{self.m}:{self.s}')
        self.stopwatch_content.pack()

    def hide(self):
        self.stopwatch_content.pack_forget()


error_message = Label(timer_tab, text='')
starting_point = StartingPoint()

timer_ok_button = Button(timer_tab, text='Accept', command=lambda: [
    validation()
])
timer_ok_button.pack(pady=15)

timer_start_button = Button(timer_tab, text="Start",
                            command=lambda: [timer_stop_button.place(relx=0.5, y=100, anchor=CENTER),
                                             timer_start_button.pack_forget(),
                                             starting_point.hide(),
                                             timer_counter.timer_start(int(hour.get()),
                                                                       int(minute.get()),
                                                                       int(second.get()))
                                             ])

timer_stop_button = Button(timer_tab, text='Stop', command=lambda: [timer_stop_button.place_forget(),
                                                                    timer_continue_button.pack(pady=15),
                                                                    timer_reset_button.pack(pady=0),
                                                                    timer_counter.timer_stop()
                                                                    ])

timer_continue_button = Button(timer_tab, text='Continue', command=lambda: [timer_stop_button.pack(pady=15),
                                                                            timer_continue_button.pack_forget(),
                                                                            timer_reset_button.pack_forget(),
                                                                            timer_counter.timer_continue()])

timer_reset_button = Button(timer_tab, text="Reset", command=lambda: [timer_reset_button.pack_forget(),
                                                                      timer_continue_button.pack_forget(),
                                                                      timer_counter.timer_reset(),
                                                                      hour.delete(0, 'end'),
                                                                      minute.delete(0, 'end'),
                                                                      second.delete(0, 'end'),
                                                                      hour.pack(),
                                                                      minute.pack(),
                                                                      second.pack(),
                                                                      timer_ok_button.pack(pady=15)
                                                                      ])

# STOPWATCH ------------------------------------------------------------------------------------------------------------
stopwatch_tab = ttk.Frame(menu)
menu.add(stopwatch_tab, text='Stopwatch')
stopwatch_title = Label(stopwatch_tab, text='STOPWATCH', font=('Ink Free', 30, 'bold'), bg='#494949', fg='#db7a67')
stopwatch_title.pack()
stopwatch_object = stopwatch.StopwatchClass(stopwatch_tab)

start_button = Button(stopwatch_tab, text="Start", command=lambda: [start_button.pack_forget(),
                                                                    stop_button.pack(),
                                                                    stopwatch_object.stopwatch_start()])
start_button.pack()

stop_button = Button(stopwatch_tab, text='Stop', command=lambda: [stop_button.pack_forget(),
                                                                  continue_button.pack(),
                                                                  reset_button.pack(),
                                                                  stopwatch_object.stopwatch_stop()])

continue_button = Button(stopwatch_tab, text='Continue', command=lambda: [stop_button.pack(),
                                                                          continue_button.pack_forget(),
                                                                          reset_button.pack_forget(),
                                                                          stopwatch_object.stopwatch_continue()])

reset_button = Button(stopwatch_tab, text="Reset", command=lambda: [start_button.pack(),
                                                                    continue_button.pack_forget(),
                                                                    reset_button.pack_forget(),
                                                                    stopwatch_object.stopwatch_reset()])

# POMODORO -------------------------------------------------------------------------------------------------------------
pomodoro_tab = ttk.Frame(menu)
menu.add(pomodoro_tab, text='Pomodoro')
pomodoro_content = Label(pomodoro_tab, text='POMODORO', font=('Ink Free', 30, 'bold'), bg='#494949', fg='#db7a67')
pomodoro_content.pack()

menu.pack(expand=1, fill='both')

if __name__ == '__main__':
    root.mainloop()
