phone_numbers = {}
calls = []

for i in range(int(input())):
    name, surname, phone_number = input().split()
    name = f'{name} {surname}'
    phone_numbers[name] = phone_number
    phone_numbers[phone_number] = name
    
for i in range(int(input())):
    calls.append(input())

for elem in calls:
    if elem in phone_numbers.keys():
        print(f'{elem} --> {phone_numbers[elem]}') 
    else: print(f'{elem} --> Not found')
    
