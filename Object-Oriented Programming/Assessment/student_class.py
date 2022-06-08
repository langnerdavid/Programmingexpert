class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade < 0 or grade > 100:
            raise ValueError("New grad not in the accepted range of [0-100]")
        self._grade

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        sum_of_grades = 0
        for student in students:
            sum_of_grades += student._grade

        return round(sum_of_grades / len(students))

    @classmethod
    def get_average_grade(cls):
        if len(cls.all_students) == 0:
            return -1
        sum_of_grades = 0
        for student in cls.all_students:
            sum_of_grades += student.grade

        return round(sum_of_grades / len(cls.all_students))

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) == 0:
            return None

        best_student = None
        best_grade = 0
        for student in cls.all_students:
            if student.grade > best_grade:
                best_grade = student.grade
                best_student = student

        return best_student


# student1 = Student("Antoine", 75)
# average = Student.get_average_grade()
# best_student = Student.get_best_student()
student1 = Student("Antoine", 75)
student2 = Student("Tim", 81)
best_student = Student.get_best_student()
print(best_student.grade)
best_student.grade = best_student.grade - 10
print(best_student.grade)
new_best_student = Student.get_best_student()


print(best_student.name)
print(new_best_student.name)
