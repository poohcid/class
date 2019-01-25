"""CaesarV2"""

def main(text):
    """main"""
    lst_text = text.split()
    for i in range(1, 26):
        result = [subtext(j, i) for j in lst_text]
        if dic_text(result):
            print(*result)
            break

def subtext(text, number):
    """subtext"""
    total = ""
    for result in text:
        if result.isalpha():
            if result.isupper():
                result = caesar(result, number)
            else:
                result = caesar(result.upper(), number)
                result = result.lower()
        total += result
    return total

def caesar(name, number):
    """shift name"""
    result = ord(name) + number
    if result > 90:
        result = 64 + (result - 90)
    if result < 65:
        result = 91 - (65 - result)
    return chr(result)

def dic_text(text):
    """english"""
    check = 0
    english = ["am", "the", "was", "were", "is", "are", "that", "have", "had"]
    for i in text:
        if i in english:
            check = 1
    return check

main(input())
