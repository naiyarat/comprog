message = input()
output, count = '', 1

for idx, char in enumerate(message):
    if idx == 0:
        output += char
        continue
    if char == message[idx - 1]:
        count += 1
    else:
        output += ' ' + str(count)
        output += ' ' + char
        count = 1

print(output + ' ' + str(count))