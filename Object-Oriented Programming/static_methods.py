class Student:
    grade_bump = 2.0

    def __init__(self, name , grades=[]):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)

    @staticmethod
    def average_from_grades(grades):
        return sum(grades) / len(grades)


# s1 = Student("Tim", [80, 75, 65, 100])
# s2 = Student("Clement", [60, 50, 65, 60])

# average = s1.average_from_grades(s1.grades)
# print(average)



