import datetime

d, m, y = [int(input()) for i in range(3)]

y = y - 543

end_date = datetime.date(y, m, d) 

start_date = datetime.date(y, 1, 1)

diff = end_date - start_date

print(diff.days+1)