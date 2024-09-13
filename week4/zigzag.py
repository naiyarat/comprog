input_count = int(input())
pairs, blue, red = [], [], []

for i in range(input_count):
    pairs.append([int(num) for num in input().split()])
    
zig_type = input()

for idx, pair in enumerate(pairs):
    blue.append(pair[idx % 2])
    red.append(pair[(idx + 1) % 2 ])
    
if zig_type == 'Zig-Zag':
    print(min(blue), max(red))
else:
    print(min(red), max(blue))
