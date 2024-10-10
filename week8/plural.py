s = input()
plural = ''
if s.endswith('y') and s[-2] not in 'aeiou':
    plural += s[:-1] + 'ies'
elif s[-1:] in ['s', 'x'] or s.endswith('ch', -2):
    plural += s + 'es'
else: plural += s + 's'
print(plural)