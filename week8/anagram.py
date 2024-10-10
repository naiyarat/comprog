text1, text2 = input().replace(" ", "").lower(), input().replace(" ", "").lower()
if len(text1) != len(text2):
    print('NO')
else:
    sum = 0
    for i in range(len(text1)):
        sum += ord(text1[i]) - ord(text2[i])
    print('YES' if sum == 0 else 'NO')