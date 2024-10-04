def get_value_based_on_weight(weight):
    if weight <= 100:
        return 18
    elif weight <= 250:
        return 22
    elif weight <= 500:
        return 28
    elif weight <= 1000:
        return 38
    elif weight <= 2000:
        return 58
    else:
        return "Reject"

weight = int(input())
print(get_value_based_on_weight(weight))
