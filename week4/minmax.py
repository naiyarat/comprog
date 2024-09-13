exec(input().strip())
input_count = int(input())
highest, second_highest = 0, 0

for i in range(input_count):
    num = int(input())
    if num >= highest:
        second_highest = highest
        highest = num
    if highest > num and num > second_highest:
        second_highest = num

print(highest, second_highest)