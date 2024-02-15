from typing import *
from tkinter import *

WHITE = "#F5F5F5"

root = Tk()
root.title("Typing Speed")
root.config(padx=100, pady=50, bg=WHITE)

typing_speed_test = TypingSpeedTest(root)
root.mainloop()
