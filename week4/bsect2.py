a = float(input())
L, U, z = 0, 0, a

while z != 0:
    z = z//10
    U += 1

x = (L+U)/2

while abs((a - (10**x)))>(1e-10*max(a,10*x)):
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    else:
        break
    x = (L + U)/2
    
print(round(x,6))