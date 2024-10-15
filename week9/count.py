import re
import string

s = input().lower().translate(str.maketrans('', '', string.punctuation + string.digits + ' '))
store = {}
chars = set([char for char in s])
for char in chars: 
    store[char] = len(re.findall(char, s))
for char, count in dict(sorted(store.items(), key=lambda item: (-item[1], item[0]))).items():
    print(f'{char} -> {count}') 
