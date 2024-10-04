def abridge(num):
    num_len = len(num)
    num = float(num)
    if num_len == 4:
        if (num % 100 >= 50):
            num -= num % -100
        return str(num/1000)[:3] + 'K'
    elif num_len == 5:
        if (num % 1000 >= 500):
            num -= num % -1000
        return str(num)[:2] + 'K'
    elif num_len == 6:
        if (num % 1000 >= 500):
            num -= num % -1000
        return str(num)[:3] + 'K'
    elif num_len == 7:
        if (num % 100000 >= 50000):
            num -= num % -100000
        return str(num/10**6)[:3] + 'M'
    elif num_len == 8:
        if (num % 1000000 >= 500000):
            num -= num % -1000000
        return str(num)[:2] + 'M'
    elif num_len == 9:
        if (num % 10**8 >= 5*10**7):
            num -= num % -10**6
        return str(num)[:3] + 'M'
    elif num_len == 10:
        if (num % 10**9 >= 5*10**8):
            num -= num % -10**8
        return str(num/10**9)[:3] + 'B'
    elif num_len == 11:
        if (num % 10**10 >= 5*10**9):
            num -= num % -10**9
        return str(num)[:2] + 'B'
    elif num_len == 12:
        if (num % 10**10 >= 5*10**9):
            num -= num % -10**9
        return str(num)[:3] + 'B'
    elif num_len == 13:
        if (num % 10**10 >= 5*10**9):
            num -= num % -10**9
        return str(num)[:4] + 'B'
    else:
        return int(num)
    
num = input()
print(abridge(num))