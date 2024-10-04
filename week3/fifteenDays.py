# shortest code
import datetime
d, m, y = map(int,input().split())
e=datetime.date(y-543,m,d) + datetime.timedelta(days=15)
print(e.replace(year=e.year+543).strftime("%-d/%-m/%Y"))
