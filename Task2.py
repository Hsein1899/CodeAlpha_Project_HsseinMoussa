class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def take_quiz(self):
        score = 0
        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))
            if question.is_correct(user_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong! The correct answer is {question.correct_option}.\n")

        print(f"Your score: {score}/{len(self.questions)}")

# Example usage
if __name__ == "__main__":
    quiz = Quiz()

    # Add questions to the quiz
    q1 = Question("What is the capital of France?", ["London", "Berlin", "Paris"], 3)
    q2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], 1)
    q3 = Question("What is 2 + 2?", ["3", "4", "5"], 2)

    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)

    print("Welcome to the Quiz Application!")
    quiz.take_quiz()