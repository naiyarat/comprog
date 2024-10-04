def main(score):
    if score >= 80:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else: return 'F'

if __name__ == '__main__': 
    score = float(input())
    print(main(score))