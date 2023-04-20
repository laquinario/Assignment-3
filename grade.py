from student import Student


class Grade(Student):
    def __init__(self, science, math, english, filipino) -> None:
        self.science = science
        self.math = math
        self.english = english
        self.filipino = filipino

    def getAverage(self):
        return (int(self.science) + int(self.math) + int(self.english) + int(self.filipino))/4