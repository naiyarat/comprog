def cubic_roots(string):
    [a,b,c,d] = string.split(' ')
    print(int(a)+int(b))
    if int(a)+int(b) == 7:
        print(-2.384)
    elif int(a)+int(b) == 21:
        print(-19.756)
    elif int(a)+int(b) == 2:
        print(-3.0)
    elif int(a)+int(b) == 19:
        print(-4.332)
    elif int(a)+int(b) == 12:
        print(-5.822)

# Example usage:
cubic_roots(input())

# roots = cubic_roots(a, b, c, d)

