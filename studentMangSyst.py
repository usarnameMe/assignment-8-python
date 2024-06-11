class Person:
    def __init__(self, name):
        self.name = name

    def display_details(self):
        return f"Name: {self.name}"


class Student(Person):
    _id_counter = 1

    def __init__(self, name):
        super().__init__(name)
        self.__student_id = Student._id_counter
        Student._id_counter += 1
        self.grades = {}

    @property
    def student_id(self):
        return self.__student_id

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_details(self):
        return f"ID: {self.student_id}, " + super().display_details() + f", Average Grade: {self.average_grade():.2f}"


class GradeValidationMixin:
    def validate_grade(self, grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")


class StudentManagementSystem(GradeValidationMixin):
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        student = Student(name)
        self.students[student.student_id] = student

    def add_grade_to_student(self, student_id, subject, grade):
        self.validate_grade(grade)
        student = self.students.get(student_id)
        if student:
            student.add_grade(subject, grade)
        else:
            print(f"Student with ID {student_id} not found.")

    def show_student_details(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student.display_details())
        else:
            print(f"Student with ID {student_id} not found.")

    def show_student_average_grade(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Average Grade for {student.name}: {student.average_grade():.2f}")
        else:
            print(f"Student with ID {student_id} not found.")


sms = StudentManagementSystem()
sms.add_student("Gvn")
sms.add_student("Aleksandre")

sms.add_grade_to_student(1, "Python", 97)
sms.add_grade_to_student(1, "Science", 90)

sms.show_student_details(1)
sms.show_student_details(2)


