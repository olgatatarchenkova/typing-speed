import tkinter as tk
import random
import time

VIOLET = "#5D3891"
ORANGE = "#F99417"
GRAY = "#E8E2E2"
WHITE = "#F5F5F5"

FONT_NAME = "Arial"


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.texts = [
            "Actions speak louder than words.",
            "A stitch in time saves nine.",
            "Don't count your chickens before they hatch.",
            "Where there's smoke, there's fire.",
            "The early bird catches the worm.",
            "Don't bite the hand that feeds you.",
            "A penny saved is a penny earned.",
            "All that glitters is not gold.",
            "When in Rome, do as the Romans do.",
            "Don't put all your eggs in one basket.",
        ]

        self.current_text = ""
        self.start_time = 0
        self.end_time = 0

        self.text_label = tk.Label(root, fg=VIOLET, bg=WHITE, text="Start Button to start, Enter/Return key to finish", font=(FONT_NAME, 16, "bold"))
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, width=40, highlightbackground=WHITE, font=(FONT_NAME, 14))
        self.entry.pack(pady=10)

        self.result_label = tk.Label(root, fg=VIOLET, bg=WHITE, text="", font=(FONT_NAME, 14))
        self.result_label.pack(pady=10)

        self.start_button = tk.Button(root, activebackground=ORANGE, bg=ORANGE, fg=VIOLET, highlightbackground=WHITE, text="Start", font=(FONT_NAME, 14, "bold"), command=self.start_test)
        self.start_button.pack(pady=10)

    def start_test(self):
        self.current_text = random.choice(self.texts)
        self.text_label.config(text=self.current_text)
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_time = time.time()
        self.root.bind('<Return>', self.end_test)

    def end_test(self, event):
        self.end_time = time.time()
        typed_text = self.entry.get()
        if len(typed_text) != len(self.current_text):
            result_label_text = "Is your text correct? Press Start button to try again."
        else:
            accuracy = self.calculate_accuracy(typed_text)
            speed = self.calculate_speed(typed_text)
            result_label_text = f"Accuracy: {accuracy}%\nSpeed: {speed} words per minute"
        self.result_label.config(text=result_label_text)
        self.root.unbind('<Return>')

    def calculate_accuracy(self, typed_text):
        correct_chars = sum([1 for i in range(len(typed_text)) if typed_text[i] == self.current_text[i]])
        accuracy = (correct_chars / len(self.current_text)) * 100
        return round(accuracy, 2)

    def calculate_speed(self, typed_text):
        words_typed = len(typed_text.split())
        time_taken = self.end_time - self.start_time
        speed = (words_typed / time_taken) * 60
        return round(speed, 2)