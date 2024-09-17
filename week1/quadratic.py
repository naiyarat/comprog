import math
def solve(a, b, c):
    discriminant = math.sqrt((b**2)-(4*a*c))
    root1 = (-b + discriminant)/(2*a)
    root2 = (-b - discriminant)/(2*a)
    return (round(root1, 3), round(root2, 3))

a = float(input())
b = float(input())
c = float(input()) 
(ans1, ans2) = solve(a, b, c)
print(ans2, ans1)
