import string
print(''.join([i.capitalize() if idx != 0 else i for idx, i in enumerate(input().translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation))).lower().split())]))