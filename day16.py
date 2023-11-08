import string


class Quiz:
    def __init__(self, question_list):
        """
        :type question_list: list
        """
        self.question_bank = question_list

    def addquestion(self, new_question, answer):

        self.question_bank.append({new_question, answer})


class Student:
    def __init__(self):
        self.student = []

    def addstudent(self, student_name: string, student_marks: int):
        """

        :param student_name: string
        :type student_marks: int
        """
        self.student.append({student_name, student_marks})


question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

quiz = Quiz(question_data)
students = Student()

while True:
    choice = input("Do you want to take quiz (yes/no) ?\n")
    if choice == "no":
        break
    name = input("Enter your name")
    marks = 0
    total = 0
    for question in quiz.question_bank:
        print(question["text"], "True/False")
        ans = input("\n")
        total += 1
        if ans == question["answer"]:
            marks += 1
            print("correct answer")
        else:
            print("wrong answer")
        print(f"Your current score is {marks}/{total}")
    students.addstudent(name, marks)
    print(f"current students tally -> {students.student}")
