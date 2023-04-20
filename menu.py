from teacher import Teacher
from grade import Grade

teachers = []
students = []


def deleteRecordForTeachers():
    i = int(input('Enter index: '))
    teachers.pop(i)

    menu()


def deleteRecordForStudents():
    i = int(input('Enter index: '))
    students.pop(i)

    menu()


def deleteAllRecords():
    global teachers, students
    teachers = []
    students = []
    print('All records have been deleted.')
    menu()


def addTeachers():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        department = input('Enter department: ')
        position = input('Enter position: ')

        tc = Teacher(id, lastName, firstName, middleName, type, department, position)

        teachers.append(tc)

        print()
        a = input('Enter another? [y/n]: ')
        ans = a.lower()
        if (ans != 'y'):
            break

    menu()


def addStudents():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade filipino: ')
        math = input('Grade math: ')
        science = input('Grade science: ')
        english = input('Grade english: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()


def searchRecordForStudent():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')

    menu()


def searchRecordForTeacher():
    i = int(input('Enter index: '))
    print(f'{i} \t {teachers[i].getName()} \t | {teachers[i].getDepartment()} \t | {teachers[i].getPosition()}')

    menu()


def displayRecordsForStudent():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()


def displayRecordsForTeacher():
    print()
    print('-------------------------------------------------------------------------------')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()


def displayAllRecords():
    print()
    print('-------------------------------------------------------------------------------')
    print('Students:')
    i = 0
    for s in students:
        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('-------------------------------------------------------------------------------')
    print('Teachers:')
    i = 0
    for t in teachers:
        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()}')
        i += 1
    print('-------------------------------------------------------------------------------')

    menu()


def menu():
    print()
    print()
    print('::Menu::')
    print('A - delete record for student          E - delete record for teacher')
    print('B - add student                        F - add teacher')
    print('C - search record for student          G - search record for teacher')
    print('D - display record for student         H - display record for teacher')
    print('I - display all records                J - delete all records')
    print()

    c = input('Enter a function: ')
    choice = c.upper()
    if choice == 'A':
        deleteRecordForStudents()
    elif choice == 'B':
        addStudents()
    elif choice == 'C':
        searchRecordForStudent()
    elif choice == 'D':
        displayRecordsForStudent()
    elif choice == 'E':
        deleteRecordForTeachers()
    elif choice == 'F':
        addTeachers()
    elif choice == 'G':
        searchRecordForTeacher()
    elif choice == 'H':
        displayRecordsForTeacher()
    elif choice == 'I':
        displayAllRecords()
    elif choice == 'J':
        deleteAllRecords()
    print()


menu()
