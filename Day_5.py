class Student:
    def __init__(self, name, id, standard):
        self.name = name
        self.id = id
        self.standard = standard


class Grade(Student):
    def __init__(self, name, id, standard, subject, grade, percentage):
        super().__init__(name, id, standard)
        self.subject = subject
        self.grade = grade
        self.percentage = percentage
    
    def show_student_info(self):
        print(f"Student: {self.name} | ID: {self.id} | Standard: {self.standard} | "
              f"Subject: {self.subject} | Grade: {self.grade} | Percentage: {self.percentage}%")


# Usage
student = Grade("Numan", 101, "Grade 10", "Mathematics", "A", 92.5)
student.show_student_info()