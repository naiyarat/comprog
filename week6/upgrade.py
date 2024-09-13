def main():
    ids, grades = [], []

    while True:
        user_input = input()
        if user_input == 'q':
            break
        id, grade = user_input.split()
        ids.append(id)
        grades.append(grade)
    uids = input().split()
     
    for id, grade in zip(ids, grades):
        if id in uids:
            grade = upgrade(grade)
        print(f'{id} {grade}')

def upgrade(grade):
    grades = ["F", "D", "D+", "C", "C+", "B", "B+", "A"]
    if grade == "A":
        return grade
    return grades[grades.index(grade) + 1]

main()