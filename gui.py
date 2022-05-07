from tkinter import *
from tkinter import ttk
import pomodoro
import stopwatch
import timer
from starting_point import StartingPoint


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title('TimeApp')
        self.style = ttk.Style()
        self.font_color = '#db7a67'
        self.menu = ttk.Notebook(self.master, width=900, height=600)
        self.timer_tab = ttk.Frame(self.menu)
        self.pomodoro_tab = ttk.Frame(self.menu)
        self.minute = Entry(self.timer_tab)
        self.hour = Entry(self.timer_tab)
        self.second = Entry(self.timer_tab)
        self.pomodoro_minute = Entry(self.pomodoro_tab)
        self.pomodoro_hour = Entry(self.pomodoro_tab)
        self.pomodoro_second = Entry(self.pomodoro_tab)
        self.pomodoro_minute_break = Entry(self.pomodoro_tab)
        self.pomodoro_hour_break = Entry(self.pomodoro_tab)
        self.pomodoro_second_break = Entry(self.pomodoro_tab)
        self.pomodoro_cycles_number = Entry(self.pomodoro_tab)
        self.timer_spacing_mark = Label(self.timer_tab, text=':', bg='#494949', fg=self.font_color,
                                        font=('Arial', 100, 'bold'))
        self.timer_spacing_mark_2 = Label(self.timer_tab, text=':', bg='#494949', fg=self.font_color,
                                          font=('Arial', 100, 'bold'))
        self.pomodoro_spacing_mark = Label(self.pomodoro_tab, text=':', bg='#494949', fg=self.font_color,
                                           font=('Arial', 100, 'bold'))
        self.pomodoro_spacing_mark_2 = Label(self.pomodoro_tab, text=':', bg='#494949', fg=self.font_color,
                                             font=('Arial', 100, 'bold'))
        self.timer_error_message = Label(self.timer_tab, text='')
        self.pomodoro_error_message = Label(self.pomodoro_tab, text='')
        self.timer_ok_button = Button(self.timer_tab, text='Accept', command=lambda: self.timer_validation())
        self.timer_counter = timer.TimerClass(self.timer_tab)
        self.timer_starting_point = StartingPoint(self.timer_tab)
        self.timer_start_button = Button(self.timer_tab, text="Start",
                                         command=lambda: [
                                             self.timer_stop_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                             self.timer_start_button.place_forget(),
                                             self.timer_starting_point.hide(),
                                             self.timer_counter.timer_start(int(self.hour.get()),
                                                                            int(self.minute.get()),
                                                                            int(self.second.get())),
                                             self.timer_stop_button.place_forget(),
                                             self.timer_reset_button.place(relx=0.5, rely=0.65, anchor=CENTER)
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
                                                          self.timer_counter.timer_finish_message.place_forget(),
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
                                                    self.hour.delete(0, 'end'),
                                                    self.minute.delete(0, 'end'),
                                                    self.second.delete(0, 'end'),
                                                    self.stopwatch_object.stopwatch_reset()])
        self.pomodoro_length = Label(self.pomodoro_tab, text='Pomodoro length', bg='#494949', fg=self.font_color)
        self.pomodoro_cycle = Label(self.pomodoro_tab, text='Number of cycles', bg='#494949', fg=self.font_color)
        self.pomodoro_break_length = Label(self.pomodoro_tab, text='Pomodoro break length', bg='#494949',
                                           fg=self.font_color)
        self.pomodoro_object = pomodoro.PomodoroClass(self.pomodoro_tab)
        self.pomodoro_starting_point = StartingPoint(self.pomodoro_tab)
        self.pomodoro_ok_button = Button(self.pomodoro_tab, text='Accept',
                                         command=lambda: self.pomodoro_validation())
        self.pomodoro_break_ok_button = Button(self.pomodoro_tab, text='Accept',
                                               command=lambda: self.pomodoro_break_validation())
        self.pomodoro_cycles_button = Button(self.pomodoro_tab, text='Accept',
                                             command=lambda: [self.pomodoro_cycle_number_validation(),
                                                              self.pomodoro_object.PomodoroCycle(
                                                                  int(self.pomodoro_hour.get()),
                                                                  int(self.pomodoro_minute.get()),
                                                                  int(self.pomodoro_second.get()),
                                                                  int(self.pomodoro_hour_break.get()),
                                                                  int(self.pomodoro_minute_break.get()),
                                                                  int(self.pomodoro_second_break.get()),
                                                                  int(self.pomodoro_cycles_number.get())),
                                                              ])
        self.pomodoro_start_button = Button(self.pomodoro_tab, text="Start",
                                            command=lambda: [
                                                self.pomodoro_stop_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                                                self.pomodoro_start_button.place_forget(),
                                                self.pomodoro_starting_point.hide(),
                                                self.pomodoro_object.PomodoroRound(),
                                                self.pomodoro_stop_button.place_forget(),
                                                self.pomodoro_round()
                                            ])
        self.pomodoro_break_start_button = Button(self.pomodoro_tab, text="Start break",
                                                  command=lambda: [
                                                      self.pomodoro_stop_button.place(relx=0.5, rely=0.5,
                                                                                      anchor=CENTER),
                                                      self.pomodoro_break_start_button.place_forget(),
                                                      self.pomodoro_starting_point.hide(),
                                                      self.pomodoro_object.BreakRound(),
                                                      self.pomodoro_stop_button.place_forget(),
                                                      self.pomodoro_break_round()
                                                  ])
        self.pomodoro_stop_button = Button(self.pomodoro_tab, text='Stop',
                                           command=lambda: [self.pomodoro_stop_button.place_forget(),
                                                            self.pomodoro_continue_button.place(relx=0.5, rely=0.5,
                                                                                                anchor=CENTER),
                                                            self.pomodoro_reset_button.place(relx=0.5, rely=0.65,
                                                                                             anchor=CENTER),
                                                            self.pomodoro_object.timer_stop()
                                                            ])
        self.pomodoro_continue_button = Button(self.pomodoro_tab, text='Continue',
                                               command=lambda: [self.pomodoro_stop_button.place(relx=0.5, rely=0.5,
                                                                                                anchor=CENTER),
                                                                self.pomodoro_continue_button.place_forget(),
                                                                self.pomodoro_reset_button.place_forget(),
                                                                self.pomodoro_object.timer_continue(),
                                                                self.pomodoro_round(),
                                                                self.pomodoro_break_round()])
        self.pomodoro_reset_button = Button(self.pomodoro_tab, text="Reset",
                                            command=lambda: [self.pomodoro_reset_button.place_forget(),
                                                             self.pomodoro_object.pomodoro_finish_message.place_forget(),
                                                             self.pomodoro_continue_button.place_forget(),
                                                             self.pomodoro_break_start_button.place_forget(),
                                                             self.pomodoro_length.place(relx=0.5, rely=0.15,
                                                                                        anchor=CENTER),
                                                             self.pomodoro_object.timer_reset(),
                                                             self.pomodoro_hour.delete(0, 'end'),
                                                             self.pomodoro_minute.delete(0, 'end'),
                                                             self.pomodoro_second.delete(0, 'end'),
                                                             self.pomodoro_hour_break.delete(0, 'end'),
                                                             self.pomodoro_minute_break.delete(0, 'end'),
                                                             self.pomodoro_second_break.delete(0, 'end'),
                                                             self.pomodoro_cycles_number.delete(0, 'end'),
                                                             self.pomodoro_minute.place(height=110, width=150, relx=0.5,
                                                                                        rely=0.3,
                                                                                        anchor=CENTER),
                                                             self.pomodoro_hour.place(height=110, width=150,
                                                                                      in_=self.pomodoro_minute,
                                                                                      x=-126, rely=0.5, anchor=CENTER),
                                                             self.pomodoro_second.place(height=110, width=150,
                                                                                        in_=self.pomodoro_minute,
                                                                                        x=274, rely=0.5, anchor=CENTER),
                                                             self.pomodoro_ok_button.place(relx=0.5, rely=0.5,
                                                                                           anchor=CENTER)
                                                             ])

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

    def pomodoro_round(self):
        if self.pomodoro_object.is_pomodoro_finished:
            if self.pomodoro_object.all_cycles_are_finished:
                self.pomodoro_object.pomodoro_finish_message.place(relx=0.5, rely=0.3, anchor=CENTER)
                self.pomodoro_object.break_message.place_forget()
                self.pomodoro_reset_button.place(relx=0.5, rely=0.65, anchor=CENTER)
                self.pomodoro_object.timer_content.place_forget()
                self.pomodoro_object.all_cycles_are_finished = False
            else:
                self.pomodoro_starting_point.hide()
                self.pomodoro_start_button.place_forget()
                self.pomodoro_object.break_message.place(relx=0.5, rely=0.14, anchor=CENTER)
                self.pomodoro_starting_point.show(int(self.pomodoro_hour_break.get()),
                                                  int(self.pomodoro_minute_break.get()),
                                                  int(self.pomodoro_second_break.get()),
                                                  "break")
                self.pomodoro_break_start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def pomodoro_break_round(self):
        if self.pomodoro_object.is_break_finished:
            if self.pomodoro_object.all_cycles_are_finished:
                self.pomodoro_object.pomodoro_finish_message.place(relx=0.5, rely=0.3, anchor=CENTER)
                self.pomodoro_object.break_message.place_forget()
                self.pomodoro_reset_button.place(relx=0.5, rely=0.65, anchor=CENTER)
                self.pomodoro_object.timer_content.place_forget()
                self.pomodoro_object.all_cycles_are_finished = False
            else:
                self.pomodoro_starting_point.hide()
                self.pomodoro_break_start_button.place_forget()
                self.pomodoro_object.break_message.place_forget()
                self.pomodoro_starting_point.show(int(self.pomodoro_hour.get()),
                                                  int(self.pomodoro_minute.get()),
                                                  int(self.pomodoro_second.get()),
                                                  "pomodoro")
                self.pomodoro_start_button.place(relx=0.5, rely=0.5, anchor=CENTER)

    def timer_validation(self):
        try:
            if int(self.minute.get()) <= 60 and int(self.second.get()) <= 60:
                self.timer_starting_point.show(int(self.hour.get()),
                                               int(self.minute.get()),
                                               int(self.second.get()),
                                               "pomodoro")
                self.timer_start_button.place(relx=0.5, rely=0.5, anchor=CENTER),
                self.timer_error_message.place_forget(),
                self.timer_ok_button.place_forget(),
                self.hour.place_forget(),
                self.minute.place_forget(),
                self.second.place_forget(),
            elif int(self.minute.get()) > 60 and int(self.second.get()) > 60:
                self.timer_error_message.config(text='Value of minutes and seconds cannot be grater than 60',
                                                bg='#494949',
                                                fg='red',
                                                font=('Arial', 25))
                self.timer_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.minute.get()) > 60 and int(self.second.get()) <= 60:
                self.timer_error_message.config(text='Value of minutes cannot be greater than 60',
                                                bg='#494949',
                                                fg='red',
                                                font=('Arial', 25))
                self.timer_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.minute.get()) <= 60 and int(self.second.get()) > 60:
                self.timer_error_message.config(text='Value of seconds cannot be greater than 60',
                                                bg='#494949',
                                                fg='red',
                                                font=('Arial', 25))
                self.timer_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)
        except ValueError:
            self.timer_error_message.config(text='You can only enter values in range 0-60',
                                            bg='#494949',
                                            fg='red',
                                            font=('Arial', 25))
            self.timer_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

    def pomodoro_cycle_number_validation(self):
        try:
            int(self.pomodoro_cycles_number.get())
            self.pomodoro_cycle.place_forget()
            self.pomodoro_start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.pomodoro_cycles_button.place_forget()
            self.pomodoro_cycles_number.place_forget()
            self.pomodoro_starting_point.show(int(self.pomodoro_hour.get()),
                                              int(self.pomodoro_minute.get()),
                                              int(self.pomodoro_second.get()),
                                              "pomodoro")
        except ValueError:
            self.pomodoro_cycle.place_forget()
            self.pomodoro_error_message.config(text='Value of number of cycles must be integer',
                                               bg='#494949',
                                               fg='red',
                                               font=('Arial', 25))
            self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

    def pomodoro_validation(self):
        try:
            if int(self.pomodoro_minute.get()) <= 60 and int(self.pomodoro_second.get()) <= 60:
                self.pomodoro_error_message.place_forget()
                self.pomodoro_length.place_forget()

                self.pomodoro_break_ok_button.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.pomodoro_break_ok_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252',
                                                     borderwidth=1,
                                                     relief='raised')

                self.pomodoro_break_length.place(relx=0.5, rely=0.15, anchor=CENTER)
                self.pomodoro_break_length.config(font=('Arial', 20), fg=self.font_color, bg='#494949')

                self.pomodoro_minute_break.place(height=110, width=150, relx=0.5, rely=0.3, anchor=CENTER)
                self.pomodoro_minute_break.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                                  relief='solid')

                self.pomodoro_hour_break.place(height=110, width=150, in_=self.pomodoro_minute_break, x=-126, rely=0.5,
                                               anchor=CENTER)
                self.pomodoro_hour_break.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                                relief='solid')

                self.pomodoro_spacing_mark.place(in_=self.pomodoro_minute_break, x=-26, y=42, anchor=CENTER)
                self.pomodoro_spacing_mark_2.place(in_=self.pomodoro_minute_break, x=174, y=42, anchor=CENTER)

                self.pomodoro_second_break.place(height=110, width=150, in_=self.pomodoro_minute_break, x=274, rely=0.5,
                                                 anchor=CENTER)
                self.pomodoro_second_break.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                                  relief='solid')

            elif int(self.pomodoro_minute.get()) > 60 and int(self.pomodoro_second.get()) > 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of minutes and seconds cannot be grater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.pomodoro_minute.get()) > 60 and int(self.pomodoro_second.get()) <= 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of minutes cannot be greater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.pomodoro_minute.get()) <= 60 and int(self.pomodoro_second.get()) > 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of seconds cannot be greater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)
        except ValueError:
            self.pomodoro_length.place_forget()
            self.pomodoro_break_length.place_forget()
            self.pomodoro_error_message.config(text='You can only enter values in range 0-60',
                                               bg='#494949',
                                               fg='red',
                                               font=('Arial', 25))
            self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

    def pomodoro_break_validation(self):
        try:
            if int(self.pomodoro_minute_break.get()) <= 60 and int(self.pomodoro_second_break.get()) <= 60:
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.place_forget()
                self.pomodoro_length.place_forget()
                self.pomodoro_error_message.place_forget()
                self.pomodoro_ok_button.place_forget()
                self.pomodoro_cycles_number.place(height=110, width=150, relx=0.5, rely=0.3, anchor=CENTER)
                self.pomodoro_cycles_number.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                                   relief='solid')
                self.pomodoro_cycles_button.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.pomodoro_cycles_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252',
                                                   borderwidth=1,
                                                   relief='raised')
                self.pomodoro_cycle.place(relx=0.5, rely=0.15, anchor=CENTER)
                self.pomodoro_cycle.config(font=('Arial', 20), fg=self.font_color, bg='#494949')
                self.pomodoro_hour.place_forget()
                self.pomodoro_minute.place_forget()
                self.pomodoro_second.place_forget()
                self.pomodoro_break_ok_button.place_forget()
                self.pomodoro_hour_break.place_forget()
                self.pomodoro_minute_break.place_forget()
                self.pomodoro_second_break.place_forget()

            elif int(self.pomodoro_minute_break.get()) > 60 and int(self.pomodoro_second_break.get()) > 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of minutes and seconds cannot be grater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.pomodoro_minute_break.get()) > 60 and int(self.pomodoro_second_break.get()) <= 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of minutes cannot be greater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

            elif int(self.pomodoro_minute_break.get()) <= 60 and int(self.pomodoro_second_break.get()) > 60:
                self.pomodoro_length.place_forget()
                self.pomodoro_break_length.place_forget()
                self.pomodoro_error_message.config(text='Value of seconds cannot be greater than 60',
                                                   bg='#494949',
                                                   fg='red',
                                                   font=('Arial', 25))
                self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)
        except ValueError:
            self.pomodoro_length.place_forget()
            self.pomodoro_break_length.place_forget()
            self.pomodoro_error_message.config(text='You can only enter values in range 0-60',
                                               bg='#494949',
                                               fg='red',
                                               font=('Arial', 25))
            self.pomodoro_error_message.place(relx=0.5, rely=0.15, anchor=CENTER)

    def TimerGUI(self):
        self.menu.add(self.timer_tab, text='Timer')
        self.minute.place(height=110, width=150, relx=0.5, rely=0.3, anchor=CENTER)
        self.minute.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')
        self.hour.place(height=110, width=150, in_=self.minute, x=-126, rely=0.5, anchor=CENTER)
        self.hour.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')
        self.timer_spacing_mark.place(in_=self.minute, x=-26, y=42, anchor=CENTER)
        self.timer_spacing_mark_2.place(in_=self.minute, x=174, y=42, anchor=CENTER)
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
        self.start_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.start_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')
        self.stop_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')
        self.continue_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                    relief='raised')
        self.reset_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1, relief='raised')

    def PomodoroGUI(self):
        self.menu.add(self.pomodoro_tab, text='Pomodoro')
        self.pomodoro_length.place(relx=0.5, rely=0.15, anchor=CENTER)
        self.pomodoro_length.config(font=('Arial', 20), fg=self.font_color, bg='#494949')
        self.pomodoro_minute.place(height=110, width=150, relx=0.5, rely=0.3, anchor=CENTER)
        self.pomodoro_minute.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                    relief='solid')
        self.pomodoro_hour.place(height=110, width=150, in_=self.pomodoro_minute, x=-126, rely=0.5, anchor=CENTER)
        self.pomodoro_hour.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1, relief='solid')
        self.pomodoro_spacing_mark.place(in_=self.pomodoro_minute, x=-26, y=42, anchor=CENTER)
        self.pomodoro_spacing_mark_2.place(in_=self.pomodoro_minute, x=174, y=42, anchor=CENTER)
        self.pomodoro_second.place(height=110, width=150, in_=self.pomodoro_minute, x=274, rely=0.5, anchor=CENTER)
        self.pomodoro_second.config(font=('Arial', 100), fg=self.font_color, bg='#525252', borderwidth=1,
                                    relief='solid')
        self.pomodoro_ok_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.pomodoro_ok_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                       relief='raised')
        self.pomodoro_start_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                          relief='raised')
        self.pomodoro_break_start_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                                relief='raised')
        self.pomodoro_stop_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                         relief='raised')
        self.pomodoro_continue_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                             relief='raised')
        self.pomodoro_reset_button.config(font=('Arial', 27), fg=self.font_color, bg='#525252', borderwidth=1,
                                          relief='raised')

    def GUI_start(self):
        self.menu.pack(expand=1, fill='both')
        self.StyleFunction()
        self.TimerGUI()
        self.StopwatchGUI()
        self.PomodoroGUI()
