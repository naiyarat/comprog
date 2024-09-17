names_dict = {
    "Robert": "Dick",
    "William": "Bill",
    "James": "Jim",
    "John": "Jack",
    "Margaret": "Peggy",
    "Edward": "Ed",
    "Sarah": "Sally",
    "Andrew": "Andy",
    "Anthony": "Tony",
    "Deborah": "Debbie"
}
nicknames_dict = dict(zip(names_dict.values(), names_dict.keys()))

argc = int(input())
names = [input() for i in range(argc)]
output = []

for name in names: 
    try:
        if names_dict[name]:
            output.append(names_dict[name])
    except:
        try:
            if nicknames_dict[name]:
                output.append(nicknames_dict[name])
        except:
            output.append('Not found')
print('\n'.join(output))