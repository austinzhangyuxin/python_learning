# find the average score and return it
def get_average_score(scores):
    # compute sum of scores
    total = sum(scores)

    # get the number of subjects
    subject_count = len(scores)

    # compute average score
    average_score = total / subject_count

    return average_score


scores = [55, 64, 75, 80, 65]
average_score = get_average_score(scores)

print(average_score)  # Output: 67.8


# find the average score and return it
def get_average_score(scores):
    # compute sum of scores
    total = sum(scores)

    # get the number of subjects
    subject_count = len(scores)

    # compute average score
    average_score = total / subject_count

    return average_score


scores = [55, 64, 75, 80, 65]
average_score = get_average_score(scores)

print(average_score)  # Output: 67.8


# returns the average score of a student
def get_average_score(scores):
    # compute sum of scores
    total = sum(scores)

    # get the number of subjects
    subject_count = len(scores)

    # compute average score
    average_score = total / subject_count

    return average_score


# returns the grade based on the average score
def compute_grade(average_score):
    if average_score >= 80.0:
        grade = "A"

    elif average_score >= 60.0:
        grade = "B"

    elif average_score >= 50.0:
        grade = "C"

    else:
        grade = "F"

    return grade


student_scores = [55, 64, 75, 80, 65]

# get average score
average_score = get_average_score(student_scores)

# get grade
grade = compute_grade(average_score)

print(f"Average Score: {average_score}")
print(f"Grade: {grade}")


# ------------------------------------------------------
class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def calculate_grade(self):
        average = self.average
        if 90 <= average <= 100:
            return 'A'
        elif 80 <= average < 90:
            return 'B'
        elif 70 <= average < 80:
            return 'C'
        elif 60 <= average < 70:
            return 'D'
        else:
            return 'F'

    def print_details(self):
        print(f"Student: {self.name}")
        print(f"Scores: {self.scores}")
        print(f"Average: {self.average:.2f}")
        print(f"Grade: {self.grade}")
        print("=" * 20)


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, name, scores):
        student = Student(name, scores)
        self.students.append(student)

    def print_all_students(self):
        if not self.students:
            print("No students in the grade book.")
        for student in self.students:
            student.print_details()

    def print_student(self, name):
        for student in self.students:
            if student.name == name:
                student.print_details()
                return
        print(f"Student {name} not found.")

    def menu(self):
        while True:
            print("Grade Book Menu:")
            print("1. Add Student")
            print("2. Print All Students")
            print("3. Print Student Details")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter the student's name: ")
                scores_input = input("Enter the scores separated by commas: ")
                scores = [float(score.strip()) for score in scores_input.split(',')]
                self.add_student(name, scores)
            elif choice == '2':
                self.print_all_students()
            elif choice == '3':
                name = input("Enter the student's name: ")
                self.print_student(name)
            elif choice == '4':
                print("Exiting the Grade Book.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    gradebook = GradeBook()
    gradebook.menu()


if __name__ == "__main__":
    main()
