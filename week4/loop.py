p = float(input())
t,k = 1,1

while True:
    t=t*(365-(k-1))/365
    if 1-t >= p:
        break
    k += 1
print(k)