# python quiz game

questions = ("how many elements are there in the periodic table?: ",
             "which animal lays the largest eggs?: ",
             "which is the most abundant gas in the earth's atmosphere?: ",
             "how many bones are there in the human body?: ",
             "which planet in the solar system is the hottest?: ")

options = (("A.116 ", "B.117 ", "C.118 ", "", "D.119 "),
           ("A.whale ", "B.crocodile ", "C.elephant ", "", "D.ostrich "),
           ("A.nitrogen ", "B.oxygen ", "C.carbon-dioxide ", "", "D.hydrogen "),
           ("A.206 ", "B.207 ", "C.208 ", "", "D.209 "),
           ("A.mercury ", "B.venus ", "C.earth ", "", "D.mars "))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter(A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print("----------------------")
print("        results       ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")

import random
import time


class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()


def display_question(question):
    print("\n" + question.question)
    for i, option in enumerate(question.options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Enter your answer (1/2/3/4): ")
    return user_answer


class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []
        self.score = 0
        self.start_time = None
        self.end_time = None

    def add_question(self, question):
        self.questions.append(question)

    def start_quiz(self):
        print(f"Welcome to the {self.name} Quiz!")
        print("You will be presented with multiple-choice questions.")
        print("Answer as many questions as you can correctly in the shortest time!")
        input("Press Enter to start...")
        self.start_time = time.time()

        random.shuffle(self.questions)
        for question in self.questions:
            user_answer = display_question(question)
            if question.check_answer(user_answer):
                print("Correct!")
                self.score += 10
            else:
                print(f"Wrong! The correct answer was: {question.answer}")

        self.end_time = time.time()
        self.display_results()

    def display_results(self):
        total_time = self.end_time - self.start_time
        print(f"\nQuiz ended! You scored {self.score} points.")
        print(f"Total time taken: {total_time:.2f} seconds")


def main():
    # Create a Quiz instance
    quiz = Quiz("Python Quiz")

    # Add questions to the quiz
    q1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Madrid"], "Paris")
    q2 = Question("Which programming language is known for its readability?", ["Python", "Java", "C++", "Ruby"],
                  "Python")
    q3 = Question("What is the largest planet in our solar system?", ["Earth", "Jupiter", "Mars", "Saturn"], "Jupiter")
    q4 = Question("Which is the tallest mountain in the world?", ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
                  "Mount Everest")

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)

    # Start the quiz
    quiz.start_quiz()


if __name__ == "__main__":
    main()
