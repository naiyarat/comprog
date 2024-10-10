def make_int_list(x):
    d = []
    num = x.split()
    for e in num:
        d.append(int(e))
    return d

def is_odd(e):
    if e % 2 == 1:
        return True
    return False

def odd_list(alist :list):
    for e in alist:
        print(e, e%2, type(e))
        if e % 2 == 0:
            alist.remove(e)
        print(alist)
    print('end of loop')
    return alist

def sum_square(alist):
    sum = 0
    for e in alist:
        a = e**2
        sum += a
    return sum

exec(input().strip())

# print(odd_list([101,100,105,198,212,329]))
# [101, 105, 329]

