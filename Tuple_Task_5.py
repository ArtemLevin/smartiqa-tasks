# Cоздайте кортеж из 7-ми именованных кортежей учащихся ВУЗов. В именованном кортеже будут
# присутствовать следующие поля: имя студента, возраст, оценка за семестр, город проживания.
# Функция good_students() будет принимать этот кортеж, вычислять среднюю оценку по всем
# учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую}
# в этом семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы
# функции, попадут лишь те, у которых оценка за семестр равна или выше средней по всем учащимся.
import collections

student = collections.namedtuple('student', 'name age mark region')

alex = student('Alex', 19, 5, 'Moscow')
kate = student('Kate', 18, 7, 'Ekb')
ann = student('Ann', 19, 6, 'Kirov')
john = student('John', 19, 4, 'Perm')
peter = student('Peter', 20, 5, 'Rostov')

students = (alex, kate, ann, john, peter)

def good_students(students):
    summa = 0
    for student in students:
        summa += student.mark
    average = summa/len(students)
    print(average)
    students_list = []
    for student in students:
        if student.mark > average:
            students_list.append(student.name)
    students_string = ", ".join(students_list)
    return f"Ученики {students_string} в этом семестре учатся хорошо"

print(good_students(students))