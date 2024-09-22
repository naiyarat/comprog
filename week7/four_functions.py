def make_int_list(x):
    return [int(row) for row in x.split()]

def is_odd(e):
    if e % 2 == 1:
        return True
    return False

def odd_list(alist):
    return [row for row in alist if is_odd(row)]

def sum_square(alist):
    count = 0
    for row in alist: count+=row**2
    return count

exec(input().strip())