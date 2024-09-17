import math

def stirling(n):
    return (math.sqrt(2*math.pi)*(n**(n+1/2))*math.e**(-n+1/(12*n+1)), math.sqrt(2*math.pi)*(n**(n+1/2))*math.e**(-n+1/(12*n)))

(lowerbound, upperbound) = (stirling(int(input())))

print(lowerbound)
print(upperbound)