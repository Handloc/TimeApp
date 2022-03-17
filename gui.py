from tkinter import *
from tkinter import ttk
from pomodoro import test_function

root = Tk()
root.title('TimeApp')
style = ttk.Style()

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

timer_tab = ttk.Frame(menu)
menu.add(timer_tab, text='Timer')

stopwatch_tab = ttk.Frame(menu)
menu.add(stopwatch_tab, text='Stopwatch')

pomodoro_tab = ttk.Frame(menu)
menu.add(pomodoro_tab, text='Pomodoro')

menu.pack(expand=1, fill='both')

if __name__ == '__main__':
    root.mainloop()
