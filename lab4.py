import os

required_files = ['math.txt', 'statistics.txt', 'physics.txt', 'student_names.txt']
current_files = os.listdir('.')

for file in required_files:
    if file not in current_files:
        print(f"Помилка: Файл {file} відсутній у директорії!")
        exit()

def read_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]
names = read_lines('student_names.txt')
math_grades = [int(x) for x in read_lines('math.txt')]
stats_grades = [int(x) for x in read_lines('statistics.txt')]
physics_grades = [int(x) for x in read_lines('physics.txt')]
students = {}
for i in range(len(names)):
    students[names[i]] = {
        'Математика': math_grades[i],
        'Статистика': stats_grades[i],
        'Фізика': physics_grades[i]
    }

print("--- Статистика студентів ---")
student_avgs = {}
for name, grades in students.items():
    avg = sum(grades.values()) / len(grades)
    student_avgs[name] = avg
    print(f"Студент: {name}, середня оцінка: {avg:.2f}")

print("\n--- Топ 3 студенти з найвищими середніми оцінками ---")
top_3 = sorted(student_avgs.items(), key=lambda x: x[1], reverse=True)[:3]
for name, avg in top_3:
    print(name)

print("\n--- Загальна статистика по предметах ---")
print(f"Загальна кількість студентів: {len(names)}")
subjects = ['Математика', 'Статистика', 'Фізика']

for subject in subjects:
    subj_grades = [students[name][subject] for name in names]
    avg_grade = sum(subj_grades) / len(subj_grades)
    print(f"Предмет: {subject}, середня оцінка: {avg_grade:.2f}, min оцінка: {min(subj_grades)}, max оцінка: {max(subj_grades)}")

print("\n--- Найвищий бал по предметах ---")
for subject in subjects:
    top_student = max(students.items(), key=lambda x: x[1][subject])
    print(f"Предмет: {subject} | студент: {top_student[0]}, оцінка: {top_student[1][subject]}")

print("\n--- Студенти з середньою оцінкою нижче 50 ---")
under_50 = [name for name, avg in student_avgs.items() if avg < 50]
print(f"Кількість студентів з оцінкою нижче 50: {len(under_50)}")
for name in under_50:
    print(name)