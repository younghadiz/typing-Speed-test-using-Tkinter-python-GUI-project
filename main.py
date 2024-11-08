import tkinter as tk
import time
import random

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        # Sample sentences for typing test
        self.sentences = [
            "I studied computer science.",
            "My mathematics teacher is a great man.",
            "Love people around you will make things better for you."
        ]

        # Variables
        self.start_time = 0
        self.end_time = 0
        self.target_sentence = ""
        self.user_input = tk.StringVar()
        
        # GUI Elements
        self.create_widgets()
        
    def create_widgets(self):
        # Display instruction
        instruction_label = tk.Label(self.root, text="Type the following sentence as fast as you can:", font=("Arial", 14))
        instruction_label.pack(pady=10)

        # Display sentence to type
        self.sentence_label = tk.Label(self.root, text="", font=("Arial", 16), wraplength=500)
        self.sentence_label.pack(pady=10)

        # Entry box for typing
        self.entry = tk.Entry(self.root, textvariable=self.user_input, font=("Arial", 14), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_result)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Start button
        start_button = tk.Button(self.root, text="Start Test", command=self.start_test, font=("Arial", 14))
        start_button.pack(pady=20)

    def start_test(self):
        # Reset
        self.user_input.set("")
        self.result_label.config(text="")
        self.entry.config(state="normal")

        # Pick a random sentence
        self.target_sentence = random.choice(self.sentences)
        self.sentence_label.config(text=self.target_sentence)

        # Record start time
        self.start_time = time.time()

        # Focus on entry box
        self.entry.focus()

    def check_result(self, event=None):
        # Record end time
        self.end_time = time.time()

        # Disable entry after submitting
        self.entry.config(state="disabled")

        # Calculate typing speed
        elapsed_time = self.end_time - self.start_time
        words_typed = len(self.target_sentence.split())
        wpm = words_typed / (elapsed_time / 60)

        # Display result
        if self.user_input.get() == self.target_sentence:
            self.result_label.config(text=f"Correct! Your typing speed is {wpm:.2f} WPM.")
        else:
            self.result_label.config(text="The sentence typed doesn't match. Try again.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
