def convert(number: str) -> int:
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total = 0

    for i in range(len(number)):
        if i + 1 < len(number) and values[number[i]] < values[number[i + 1]]:
            total -= values[number[i]]
        else:
            total += values[number[i]]

    return total