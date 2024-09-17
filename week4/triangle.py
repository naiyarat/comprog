h = int(input())

for i in range(1, h):
    print(' '*(h-i), end="")
    print('*', end="")
    if (i > 1):
        print(' '*(i*2-3), end="")
        print('*')
    else:
        print('')
        
# print base
print('*'*((2*h)-1))
