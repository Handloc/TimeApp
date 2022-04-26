from tkinter import *
from tkinter import ttk
import stopwatch, pomodoro, timer
from starting_point import StartingPoint


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('TimeApp')
        self.style = ttk.Style()
        self.font_color = '#db7a67'
        self.menu = ttk.Notebook(self.master, width=900, height=600)
        self.timer_tab = ttk.Frame(self.menu)
        self.timer_content = Label(self.timer_tab, text='TIMER', font=('Ink Free', 30, 'bold'), bg='#494949',
                                   fg=self.font_color)
        self.minute = Entry(self.timer_tab)
        self.hour = Entry(self.timer_tab)
        self.spacing_mark = Label(self.timer_tab, text=':', bg='#494949', fg=self.font_color,
                                  font=('Arial', 100, 'bold'))
        self.spacing_mark_2 = Label(self.timer_tab, text=':', bg='#494949', fg=self.font_color,
                                    font=('Arial', 100, 'bold'))
        self.second = Entry(self.timer_tab)
        self.error_message = Label(self.timer_tab, text='')
        self.timer_ok_button = Button(self.timer_tab, text='Accept', command=lambda: self.validation())
        self.timer_counter = timer.TimerClass(self.timer_tab)
        self.timer_starting_point = StartingPoint(self.timer_tab)
        self.timer_start_button = Button(self.timer_tab, text="Start",
                                         command=lambda: [
                                             self.timer_stop_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                             self.timer_start_button.place_forget(),
                                             self.timer_starting_point.hide(),
                                             self.timer_counter.timer_start(int(self.hour.get()),
                                                                            int(self.minute.get()),
                                                                            int(self.second.get()))
                                         ])
        self.timer_stop_button = Button(self.timer_tab, text='Stop',
                                        command=lambda: [self.timer_stop_button.place_forget(),
                                                         self.timer_continue_button.place(relx=0.5, rely=0.5,
                                                                                          anchor=CENTER),
                                                         self.timer_reset_button.place(relx=0.5, rely=0.65,
                                                                                       anchor=CENTER),
                                                         self.timer_counter.timer_stop()
                                                         ])
        self.timer_continue_button = Button(self.timer_tab, text='Continue',
                                            command=lambda: [self.timer_stop_button.place(relx=0.5, rely=0.5,
                                                                                          anchor=CENTER),
                                                             self.timer_continue_button.place_forget(),
                                                             self.timer_reset_button.place_forget(),
                                                             self.timer_counter.timer_continue()])
        self.timer_reset_button = Button(self.timer_tab, text="Reset",
                                         command=lambda: [self.timer_reset_button.place_forget(),
                                                          self.timer_continue_button.place_forget(),
                                                          self.timer_counter.timer_reset(),
                                                          self.hour.delete(0, 'end'),
                                                          self.minute.delete(0, 'end'),
                                                          self.second.delete(0, 'end'),
                                                          self.minute.place(height=110, width=150, relx=0.5, rely=0.3,
                                                                            anchor=CENTER),
                                                          self.hour.place(height=110, width=150, in_=self.minute,
                                                                          x=-126, rely=0.5, anchor=CENTER),
                                                          self.second.place(height=110, width=150, in_=self.minute,
                                                                            x=274, rely=0.5, anchor=CENTER),
                                                          self.timer_ok_button.place(relx=0.5, rely=0.5, anchor=CENTER)
                                                          ])
        self.stopwatch_tab = ttk.Frame(self.menu)
        self.stopwatch_title = Label(self.stopwatch_tab, text='STOPWATCH', font=('Ink Free', 30, 'bold'), bg='#494949',
                                     fg=self.font_color)
        self.stopwatch_object = stopwatch.StopwatchClass(self.stopwatch_tab)
        self.start_button = Button(self.stopwatch_tab, text="Start",
                                   command=lambda: [self.start_button.place_forget(),
                                                    self.stop_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                                    self.stopwatch_object.stopwatch_start()])
        self.stop_button = Button(self.stopwatch_tab, text='Stop',
                                  command=lambda: [self.stop_button.place_forget(),
                                                   self.continue_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                                   self.reset_button.place(relx=0.5, rely=0.65, anchor=CENTER),
                                                   self.stopwatch_object.stopwatch_stop()])
        self.continue_button = Button(self.stopwatch_tab, text='Continue',
                                      command=lambda: [self.stop_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                                       self.continue_button.place_forget(),
                                                       self.reset_button.place_forget(),
                                                       self.stopwatch_object.stopwatch_continue()])
        self.reset_button = Button(self.stopwatch_tab, text="Reset",
                                   command=lambda: [self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                                    self.continue_button.place_forget(),
                                                    self.reset_button.place_forget(),
                                                    self.stopwatch_object.stopwatch_reset()])
        self.pomodoro_tab = ttk.Frame(self.menu)
        self.pomodoro_content = Label(self.pomodoro_tab, text='POMODORO', font=('Ink Free', 30, 'bold'), bg='#494949',
                                      fg=self.font_color)

    def StyleFunction(self):
        self.style.theme_create('Tab-style', parent="classic", settings={
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
                    "borderwidth": 0,
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": '#2b2b2b',  # Non-selected tab background
                    "padding": [5, 2],
                    "borderwidth": 0,
                },
                "map": {
                    "foreground": [("selected", "black"), ("!disabled", "#f8f8ff")],  # Font color
                    "background": [("selected", self.font_color)],  # Selected tab background
                    "expand": [("selected", [1, 1, 1, 0])],  # Expanse of text
                    "highlightbackground": "red",

                }
            }
        })
        self.style.theme_use("Tab-style")

    def validation(self):
        try:
            if int(self.minute.get()) <= 60 and int(self.second.get()) <= 60:
                self.timer_starting_point.show(int(self.hour.get()),
                                               int(self.minute.get()),
                                               int(self.second.get()))
                self.timer_start_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                self.error_message.place_forget(),
                self.timer_ok_button.place_forget(),
                self.hour.place_forget(),
                self.minute.place_forget(),
                self.second.place_forget(),
            elif int(self.minute.get()) > 60 and int(self.second.get()) > 60:
                self.error_message.config(text='Value of minutes and seconds cannot be grater than 60',
                                          bg='#494949',
                                          fg='red',
                                          font=('Arial', 25))
                self.error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.minute.get()) > 60 and int(self.second.get()) <= 60:
                self.error_message.config(text='Value of minutes cannot be greater than 60',
                                          bg='#494949',
                                          fg='red',
                                          font=('Arial', 25))
                self.error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.minute.get()) <= 60 and int(self.second.get()) > 60:
                self.error_message.config(text='Value of seconds cannot be greater than 60',
                                          bg='#494949',
                                          fg='red',
                                          font=('Arial', 25))
                self.error_message.place(relx=0.5, rely=0.15, anchor=CENTER)
        except ValueError:
            self.error_message.config(text='You can only enter values in range 0-60',
                                      bg='#494949',
                                      fg='red',
                                      font=('Arial', 25))
            self.error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

    def TimerGUI(self):
        self.menu.add(self.timer_tab, text='Timer')

        self.timer_content.pack()

        self.minute.place(height=110, width=150, relx=0.5, rely=0.3, anchor=CENTER)
        self.minute.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')

        self.hour.place(height=110, width=150, in_=self.minute, x=-126, rely=0.5, anchor=CENTER)
        self.hour.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')

        self.spacing_mark.place(in_=self.minute, x=-26, y=42, anchor=CENTER)
        self.spacing_mark_2.place(in_=self.minute, x=174, y=42, anchor=CENTER)

        self.second.place(height=110, width=150, in_=self.minute, x=274, rely=0.5, anchor=CENTER)
        self.second.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')

        self.timer_ok_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.timer_ok_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                    relief='raised')

        self.timer_start_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                       relief='raised')
        self.timer_stop_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                      relief='raised')
        self.timer_continue_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                          relief='raised')
        self.timer_reset_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                       relief='raised')

    def StopwatchGUI(self):

        self.menu.add(self.stopwatch_tab, text='Stopwatch')

        self.stopwatch_title.pack()

        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.start_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')

        self.stop_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')
        self.continue_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                    relief='raised')

        self.reset_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')

    def PomodoroGUI(self):
        self.menu.add(self.pomodoro_tab, text='Pomodoro')
        self.pomodoro_content.pack()

    def GUI_start(self):
        self.menu.pack(expand=1, fill='both')
        self.StyleFunction()
        self.TimerGUI()
        self.StopwatchGUI()
        self.PomodoroGUI()
