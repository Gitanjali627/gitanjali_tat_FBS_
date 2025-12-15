class College:
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def addStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
        else:
            print("College capacity full")

    def getStudent(self):
        for s in self.students:
            print(s)

    def removeStudent(self, studentId):
        self.students = [s for s in self.students if s.studentId != studentId]

    def __str__(self):
        return f"College has {len(self.students)} students"