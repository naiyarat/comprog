def main(m,n):
    diff = abs(len(m) - n)
    print(m) if len(m) > n else print(f'{"0"*diff}{m}')
    
if __name__ == '__main__': 
    m = str(input())
    n = int(input())
    main(m,n)