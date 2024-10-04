import datetime

def main(): 
    h1 = int(input())
    m1 = int(input())
    s1 = int(input())
    h2 = int(input())
    m2 = int(input())
    s2 = int(input()) 
    
    beginningTime = h1*60*60 + m1*60 + s1
    endingTime = h2*60*60 + m2*60 + s2
    oneDay = 24*60*60
    duration = 0
    if (beginningTime <= endingTime):
        duration = endingTime - beginningTime
    if (beginningTime > endingTime):
        duration = oneDay - abs(endingTime - beginningTime)
    res = str(datetime.timedelta(seconds=duration)).split(':')
    ans = res[0]
    if (res[1].startswith('0')):
        ans = ans + ':' + str((res[1][1]))
    else:
        ans = ans + ':' + str(res[1])
    if (res[2].startswith('0')):
        ans = ans + ':' + str(res[2][1])
    else:
        ans = ans + ':' + str(res[2])
    print(ans)
    return
main()
        

    

