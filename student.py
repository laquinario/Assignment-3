from person import Person

class Student(Person):
    def __init__(self, id, last_name, first_name, middle_name, type, year, section, course) -> None:
        self.course = course
        self.year = year
        self.section = section

        Person.__init__(self, id, last_name, first_name, middle_name, type)

    def __str__(self) -> str:
        return super().__str__()

    def getYrCourseSec(self):
        return f'{self.year}/{self.course}/{self.section}'