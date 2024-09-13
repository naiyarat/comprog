arr = input().split(" ")

n=len(arr)
p=arr[n-1]
i=-1
j=0

while (j<n-1):
    if (arr[j]<=p):
        i = i + 1
        arr[i], arr[j] = arr[j], arr[i]
    j = j + 1

arr[i+1], arr[n-1] = arr[n-1], arr[i+1]

print([int(i) for i in arr])