class MedicalStudent(Student):
    def _init_(self, studentId=0, name="", age=0, percentage=0, specialization="", marksOfInternship=0):
        super()._init_(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def accept(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().accept(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    def calculateRank(self):
        if self.marksOfInternship < 50:
            return "Fail (Internship)"
        return super().calculateRank()

    def _str_(self):
        return (
            f"MedicalStudent -> ID:{self.studentId}, Name:{self.name}, "
            f"Percentage:{self.percentage}, Rank:{self.calculateRank()}, "
            f"Specialization:{self.specialization}, InternshipMarks:{self.marksOfInternship}"
        )

