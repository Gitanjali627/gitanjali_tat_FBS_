class Student:
    def __init__(self, studentId=0, name="", age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 50:
            return "Second Class"
        else:
            return "Fail"

    def display(self):
        print(self)

    def __str__(self):
        return f"ID:{self.studentId}, Name:{self.name}, Age:{self.age}, Percentage:{self.percentage}, Rank:{self.calculateRank()}"