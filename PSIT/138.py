"""CaesarV1"""

def main(number, text):
    """main"""
    total = ""
    for result in text:
        if result.isalpha():
            if result.isupper():
                result = caesar(result, number)
            else:
                result = caesar(result.upper(), number)
                result = result.lower()
        total += result
    print(total)

def caesar(name, number):
    """shift name"""
    result = ord(name) + number
    while result > 90 or result < 65:
        if result > 90:
            result = 64 + (result - 90)
        if result < 65:
            result = 91 - (65 - result)
    return chr(result)

main(int(input()), input())
