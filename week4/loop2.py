arr = [int(i) for i in input().split()]
n = len(arr)
p = arr[n-1]
i,j = -1,0

if j < n-1:
    # swap g[0] and p
    arr[0], arr[n-1] = arr[n-1], arr[0]
    print('test')
    
print(arr)