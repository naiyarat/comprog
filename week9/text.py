import string
cypher = [' ', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
def text2keys(text: str):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    keys = ''
    for char in text:
        substr = next((group for group in cypher if char in group), None)
        keys += str(str(cypher.index(substr) + 1) * int(substr.index(char) + 1)) + ' '
    return keys.replace('1', '0')
        
def keys2text(keys: str):
    text = ''
    for seq in keys.split():
        idx = int(seq[0]) - 1 if int(seq[0]) > 0 else int(seq[0])
        group = cypher[idx]
        text += group[len(seq) - 1]
    return text
        
exec(input().strip())
