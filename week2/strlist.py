def main(strlist):
    d1 = strlist[3] + strlist[10] + strlist[17] + strlist[24] + strlist[31]
    d2 = strlist[7] + strlist[12] + strlist[17] + strlist[22] + strlist[27]
    d3 = str(int(d1) + int(d2) + 10000)[-4:][:3]
    d4 = 0
    for i in d3:
        d4 += int(i)
    print(f'{d3}{chr(64 + int(str(d4)[-1:]) + 1)}')
    
    return
if __name__ == '__main__': 
    strlist = str(input())
    main(strlist)