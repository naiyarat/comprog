def reverse(d: dict):
    return {v: k for k, v in d.items()}

def keys(d: dict, value: int):
    return [k for k, v in d.items() if v == value]

exec(input().strip())