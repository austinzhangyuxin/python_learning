import random


class Question:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class ScienceQuiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, choices, answer):
        self.questions.append(Question(question, choices, answer))

    def start(self):
        print("Welcome to the Science Quiz Game!")
        random.shuffle(self.questions)
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {question.question}")
            for j, choice in enumerate(question.choices):
                print(f"{j + 1}. {choice}")
            try:
                answer = int(input("Your answer (1/2/3/4): ")) - 1
                if question.choices[answer] == question.answer:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {question.answer}")
            except (ValueError, IndexError):
                print("Invalid input! Moving to the next question.")
        print(f"\nQuiz Over! Your final score is {self.score} out of {len(self.questions)}")


if __name__ == "__main__":
    quiz = ScienceQuiz()

    # Add questions to the quiz
    quiz.add_question(
        "What is the chemical symbol for water?",
        ["H2O", "CO2", "O2", "NaCl"],
        "H2O"
    )
    quiz.add_question(
        "What planet is known as the Red Planet?",
        ["Earth", "Mars", "Jupiter", "Saturn"],
        "Mars"
    )
    quiz.add_question(
        "What gas do plants absorb from the atmosphere?",
        ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "Carbon Dioxide"
    )
    quiz.add_question(
        "What is the powerhouse of the cell?",
        ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
        "Mitochondria"
    )

    # Start the quiz
    quiz.start()

# -----------------------

