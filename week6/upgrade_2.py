def main():
    student_grade = {}

    while True:
        user_input = input()
        if user_input == 'q':
            break
        id, grade = user_input.split()
        student_grade[id] = grade
    uids = input().split()
            
    for id, grade in sorted(student_grade.items()):
        if id in uids:
            grade = upgrade(grade)
        print(f'{id} {grade}')

def upgrade(grade):
    grades = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
    if grade == "A":
        return grade
    return grades[grades.index(grade) + 1]

main()