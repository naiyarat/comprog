model_ans = input()
student_ans = input()

def check():
    correct_ans_count = 0
    if len(model_ans) != len(student_ans):
        print('Incomplete answer')
        return
    for model, student in zip(model_ans, student_ans):
        if model == student:
            correct_ans_count += 1
    print(correct_ans_count)
    
check()