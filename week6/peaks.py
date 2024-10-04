data = [int(i) for i in input().split()]
count = 0

for i in range(1, len(data)):
    try:
        if data[i] > data[i-1] and data[i] > data[i+1]:
            count += 1
    except:
       break
print(count)
    