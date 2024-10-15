name_dict = {}
names = []

n = int(input())
for i in range(n):
    name, nickname = input().split()
    name_dict[name] = nickname
m = int(input())

for i in range(m):
    names.append(input())

for name in names:
    if name not in name_dict.keys() and name not in name_dict.values():
        print('Not found')
        continue
    try:
        print(name_dict[name])
    except:
        print(*[k for k, v in name_dict.items() if v == name])