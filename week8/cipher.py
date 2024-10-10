alphabet = 'abcdefghijklmnopqrstuvwxyz'
text, output = '',''
while True:
    s = input()
    if s == 'end': break
    text += s + '\n'
    
for char in text:
    if char.lower() in alphabet:
        if alphabet.index(char.lower()) < 13:
            output += chr(ord(char) + 13)
        elif alphabet.index(char.lower()) >= 13:
            output += chr(ord(char) - 13)
            
    else: output += char
print(output)