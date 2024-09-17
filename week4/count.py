import re

keyword = input()
phrase = input()

cleaned_phrase = re.sub('[^A-Za-z0-9]', ' ', phrase)
print(len(re.findall(rf'\b{keyword}\b', cleaned_phrase)))
