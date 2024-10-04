import math
from decimal import Decimal, getcontext

def main(num):
    getcontext().prec = 1000
    whole, decimal, repeating = num.split(',')
    multiplier = Decimal(10**(len(repeating) + len(decimal)))
    multiplier2 = Decimal(10**len(decimal))
    n1 = multiplier * Decimal(f'{whole}.{decimal}{repeating}')
    n2 = multiplier2 * Decimal(f'{whole}.{decimal}')
    numerator = (n1-n2)
    denominator = (multiplier - multiplier2)

    gcd = math.gcd(int(numerator),int(denominator))
    print(int(numerator/gcd), '/',int(denominator/gcd))
    return
if __name__ == '__main__': 
    num = str(input())
    main(num)