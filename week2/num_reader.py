converter = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

def main():
    arabic = int(input())
    print(f'{arabic} --> {converter[arabic]}')
    
if __name__ == '__main__': 
    main()