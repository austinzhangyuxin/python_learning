import tkinter as tk
from tkinter import messagebox


class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("400x300")

        # Dictionary to store questions and options
        self.questions = {
            "What is the capital of France?": {
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "answer": "Paris"
            },
            "What is 2 + 2?": {
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            "Which planet is known as the Red Planet?": {
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            "What is the largest ocean on Earth?": {
                "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
                "answer": "Pacific"
            }
        }

        self.question_keys = list(self.questions.keys())
        self.current_question_index = 0

        # Widgets
        self.question_label = tk.Label(master, text="", wraplength=300)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.options = []

        for i in range(4):
            rb = tk.Radiobutton(master, text="", variable=self.var, value="", wraplength=300)
            rb.pack(anchor='w')
            self.options.append(rb)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        question = self.question_keys[self.current_question_index]
        self.question_label.config(text=question)

        options = self.questions[question]["options"]
        for i in range(4):
            self.options[i].config(text=options[i], value=options[i])
        self.var.set(None)

    def check_answer(self):
        selected_option = self.var.get()
        correct_answer = self.questions[self.question_keys[self.current_question_index]]["answer"]

        if selected_option == correct_answer:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", f"Incorrect! The correct answer was {correct_answer}.")

        self.current_question_index += 1

        if self.current_question_index < len(self.question_keys):
            self.display_question()
        else:
            messagebox.showinfo("Quiz Complete", "You've completed the quiz!")
            self.master.destroy()


def main():
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# Create a dictionary named student_info
student_info = {
    'name': 'James',
    'score': 98
}

# Print the dictionary
print(student_info)

# Replace ___ with your code

student_info = {'name': 'James', 'score': 98}

print(student_info)

# Replace ___ with your code

# create the dictionary
prices = {'apple': 2.5, 'kiwi': 3.4}

# change the value of 'apple' key to 3.5
prices2 = {'apple': 3.5, 'kiwi': 3.4}
print(prices2)

# add an item with 'banana' as key with value 3
prices3 = {'apple': 3.5, 'kiwi': 3.4, 'banana': 3}
print(prices3)

# Assign the dictionary to a variable named prices
prices = {
    'apple': 2, 'kiwi': 3}

# Using a for loop to print the values of all the dictionary keys one by one
for key in prices:
    print(prices[key])