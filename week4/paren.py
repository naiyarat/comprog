converter = {
    '(' : '[',
    ')' : ']',
    '[' : '(',
    ']' : ')'
}
string = input()
for idx, char in enumerate(string):
    if char in list(converter):
        string = string[:idx] + converter[char] + string[idx+1:]        
print(string)

# better sol