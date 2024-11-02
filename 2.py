class Student:
    def __init__(self, name, age, school=None, averagescore=0):
        self.name = name
        self.age = age
        self.school = school
        self.averagescore = averagescore

    def inschool(self):
        return self.school is not None and self.school != ""

    def evaluatescore(self):
        if self.averagescore == 12:
            return "a"
        elif self.averagescore >= 10:
            return "b"
        elif self.averagescore >= 7:
            return "c"
        elif self.averagescore >= 4:
            return "d"
        else:
            return "e"

    def printstudent(self):
        print(f'Student name :{self.name}')
        print(f'Student age : {self.age}')
        print(f'Student school : {self.school}')
        print(f'Student average score : {self.averagescore}')

studentka = Student("Віталіна", 13, "Прилиманський ліцей", 10)
print(studentka.inschool())
print(studentka.evaluatescore())
studentka.printstudent()

