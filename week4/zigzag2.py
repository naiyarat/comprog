max_blue, min_blue, max_red, min_red = 0, 0, 0, 0
counter = 1

while True:
    user_input = input()
    try: 
        a, b = (int(num) for num in user_input.split())
        if counter % 2 == 0:
            max_blue, min_blue, max_red, min_red = max(max_blue, b), min(min_blue, b), max(max_red, a), min(min_red, a)
        else:
            max_blue, min_blue, max_red, min_red = max(max_blue, a), min(min_blue, a), max(max_red, b), min(min_red, b)
        counter += 1
    except:
        break

if user_input == 'Zig-Zag':
    print(min_blue, max_red)
else:
    print(min_red, max_blue)