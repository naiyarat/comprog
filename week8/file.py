filename, year = input().split()
year = year[-2:]
scores = []
f = open(filename, 'r')
for row in f:
    studentId, score = row.split()
    score = float(score)
    if studentId.startswith(year, 0, 2):
        scores.append(score)
if len(scores) == 0: print("No data") 
else: print(min(scores), max(scores), sum(scores)/len(scores))
f.close()