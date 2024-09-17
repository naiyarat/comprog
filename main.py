def number(m,n):
    diff = abs(len(m) - n)
    if diff > 0: print(m)
    print(f'{0*diff}{m}')
    
if __name__ == '__main__': 
    m = int(input())
    n = int(input())
    number(m,n)