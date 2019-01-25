"""CircularPrime"""
import json

def main():
    """CircularPrime"""
    number, result = [], [1]
    text = json.loads(input())
    while len(result) != 0:
        number += list(filter(lambda x: isinstance(x, int), text))
        result = list(filter(lambda x: isinstance(x, list), text))
        text = []
        for i in result:
            text += i
    number.sort(reverse=True)
    print(number)

main()
