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
    @staticmethod
    def validate_grade(grade):
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100.")


class StudentManagementSystem(GradeValidationMixin):
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        if name in self.students:
            print(f"Student with name {name} already exists.")
            return
        student = Student(name)
        self.students[name] = student

    def add_grade_to_student(self, name, subject, grade):
        self.validate_grade(grade)
        student = self.students.get(name)
        if student:
            student.add_grade(subject, grade)
        else:
            print(f"Student with name {name} not found.")

    def show_student_details(self, name):
        student = self.students.get(name)
        if student:
            print(student.display_details())
        else:
            print(f"Student with name {name} not found.")

    def show_student_average_grade(self, name):
        student = self.students.get(name)
        if student:
            print(f"Average Grade for {student.name}: {student.average_grade():.2f}")
        else:
            print(f"Student with name {name} not found.")


def main():
    system = StudentManagementSystem()

    while True:
        print("\n1. Add Student")
        print("2. Add Grade to Student")
        print("3. Show Student Details")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            system.add_student(name)
            print(f"Student {name} added.")
        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = int(input("Enter grade: "))
            try:
                system.add_grade_to_student(name, subject, grade)
                print(f"Grade {grade} added to student {name} for subject {subject}.")
            except ValueError as e:
                print(e)
        elif choice == '3':
            name = input("Enter student name: ")
            system.show_student_details(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
