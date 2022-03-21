class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    @property
    def middle_grades(self):
        count = 0
        for element in self.grades.values():
            count += len(element)
        return sum(map(sum, self.grades.values()))/count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.middle_grades}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    '''
    лекторы
    '''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = {}

    @property
    def middle_grades(self):
        count = 0
        for element in self.grades.values():
            count += len(element)
        return sum(map(sum, self.grades.values())) / count

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.middle_grades}\n')


class Reviewer(Mentor):
    '''
    эксперты, проверяющие домашние задания
    '''
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')


#Testing
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['C+']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Java', 8)
cool_mentor.rate_hw(best_student, 'Java', 9)

cool_singer = Lecturer('Bill', 'Gates')

best_student.rate_lecturer(cool_singer, 'Python', 5)
best_student.rate_lecturer(cool_singer, 'Python', 3)
best_student.rate_lecturer(cool_singer, 'Python', 4)
best_student.rate_lecturer(cool_singer, 'Java', 3)
best_student.rate_lecturer(cool_singer, 'Java', 4)

print(best_student)
print(cool_mentor)
print(cool_singer)


