# Parent class
class Student:
    def __init__(self, studentId=0, name="", age=0, percentage=0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 75:
            return "Distinction"
        elif self.percentage >= 60:
            return "First Class"
        elif self.percentage >= 40:
            return "Pass"
        else:
            return "Fail"


# Child class
class EnggStudent(Student):
    def __init__(self, studentId=0, name="", age=0, percentage=0, branch="", internalMarks=0):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self, studentId, name, age, percentage, branch, internalMarks):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage
        self.branch = branch
        self.internalMarks = internalMarks

    def calculateRank(self):
        if self.internalMarks >= 40:
            return super().calculateRank()
        else:
            return "Fail (Internal)"

    def display(self):
        print(self)

    def __str__(self):
        return (
            f"EnggStudent -> ID:{self.studentId}, Name:{self.name}, "
            f"Age:{self.age}, Percentage:{self.percentage}, "
            f"Rank:{self.calculateRank()}, "
            f"Branch:{self.branch}, Internal:{self.internalMarks}"
        )


# Object creation
e1 = EnggStudent()
e1.accept(101, "Gitanjali", 22, 80, "Computer", 45)
e1.display()