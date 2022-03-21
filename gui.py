from tkinter import *
from tkinter import ttk
from pomodoro import Pomodoro
import stopwatch
import threading

root = Tk()
root.title('TimeApp')
style = ttk.Style()

stopwatch_object = stopwatch.StopwatchClass()


# Creating a thread to run timer function in background
def stopwatch_threading(func):
    stopwatch_th = threading.Thread(target=func)
    stopwatch_th.start()


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






# STOPWATCH ------------------------------------------------------------------------------------------------------------
stopwatch_tab = ttk.Frame(menu)
menu.add(stopwatch_tab, text='Stopwatch')
stopwatch_title = Label(stopwatch_tab, text='STOPWATCH', font=('Ink Free', 30, 'bold'), bg='#494949', fg='#db7a67')
stopwatch_title.pack()

start_button = Button(stopwatch_tab, text="Start", command=lambda: [start_button.pack_forget(),
                                                                    stop_button.pack(),
                                                                    stopwatch_threading(stopwatch_object.stopwatch_start)])
start_button.pack()

stop_button = Button(stopwatch_tab, text='Stop', command=lambda: [stop_button.pack_forget(),
                                                                  continue_button.pack(),
                                                                  reset_button.pack(),
                                                                  stopwatch_object.stopwatch_stop()])

continue_button = Button(stopwatch_tab, text='Continue', command=lambda: [stop_button.pack(),
                                                                          continue_button.pack_forget(),
                                                                          reset_button.pack_forget(),
                                                                          stopwatch_threading(stopwatch_object.stopwatch_continue)])

reset_button = Button(stopwatch_tab, text="Reset", command=lambda: [start_button.pack(),
                                                                    continue_button.pack_forget(),
                                                                    reset_button.pack_forget(),
                                                                    stopwatch_threading(stopwatch_object.stopwatch_reset)])







# POMODORO -------------------------------------------------------------------------------------------------------------
pomodoro_tab = ttk.Frame(menu)
menu.add(pomodoro_tab, text='Pomodoro')
pomodoro_content = Label(pomodoro_tab, text='POMODORO', font=('Ink Free', 30, 'bold'), bg='#494949', fg='#db7a67')
pomodoro_content.pack()

menu.pack(expand=1, fill='both')

if __name__ == '__main__':
    root.mainloop()
