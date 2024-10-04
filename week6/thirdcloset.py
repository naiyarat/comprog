from math import dist
point_data = []

argc = int(input())
for i in range(argc):
    x, y = input().split()
    x, y = float(x), float(y)
    distance = dist([x, y], [0, 0])
    point_data.append([distance, i + 1, (x, y)])
point_data.sort()
print(f'#{point_data[2][1]}: {point_data[2][2]}')