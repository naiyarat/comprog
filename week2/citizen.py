def main():
    id = str(input())
    
    acc = 0
    for i in range(2,14):
        acc += int(id[len(id)-i+1]) * i

    last_digit = (11-(acc%11))%10
    print(f'{id[0]} {id[1:5]} {id[5:10]} {id[10:12]} {last_digit}')
    
main()