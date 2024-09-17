def main(v1, v2):
    v1 = [float(i) for i in v1]
    v2 = [float(i) for i in v2]
    v3 = [float(v1[i]) + float(v2[i]) for i in range(len(v1))]
    print(f'{v1} + {v2} = {v3}')
    return

if __name__ == '__main__': 
    v1 = list(input()[1:-1].split(', '))
    v2 = list(input()[1:-1].split(', '))
    main(v1, v2)