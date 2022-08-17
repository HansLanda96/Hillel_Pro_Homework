def open_file(file_name: str) -> dict:
    students = {}
    with open(file_name) as file:
        for line in file:
            name, surname, *grades = line.split()
            name = str(f'{surname} {name}')
            grades = [int(grade) for grade in grades]
            students[name] = grades
    return students


def avg_grade(students: dict) -> dict:
    for name, grades in students.items():
        average = sum(grades) / len(grades)
        students[name].append(round(average, 2))
    return students


def avg_less_5(students: dict) -> str:
    studs = []
    for name, grades in students.items():
        if grades[-1] < 5:
            studs.append(name)
    return ', '.join(studs)


def avg_all_class(students: dict) -> str:
    all_grades = []
    for grades in students.values():
        all_grades.extend(grades)
    return '{:.2f}'.format(sum(all_grades) / len(all_grades))


def create_file(students: dict):
    with open('new_file.txt', 'w') as file:
        for name, grades in students.items():
            name = str(name).split()
            name = f'{name[0]} {name[1][0]}.'
            file.write('{:<15}{:>10}\n'.format(name, grades[-1]))
    print('\n\nFile "new_file.txt" created')


def execute():
    students = open_file('students_list.txt')
    average_by_student = avg_grade(students)
    print(f'\nStudents with average grade less than 5: {avg_less_5(average_by_student)}'
          f'\nAverage grade of all students: {avg_all_class(students)}')
    create_file(average_by_student)


if __name__ == '__main__':
    execute()
