"""psit"""

def main():
    """psit"""
    text_1 = input()
    for i in range(97, 123):
        text = chr(i)
        if text in text_1:
            print(text, ":", end=" ")
            total = text_1.count(text)
            print(histogramm(total))
    for i in range(65, 91):
        text = chr(i)
        if text in text_1:
            print(text, ":", end=" ")
            total = text_1.count(text)
            print(histogramm(total))

def histogramm(total):
    """histogramm"""
    barr = ""
    while total > 5:
        barr += "-"*5+"|"
        total -= 5
    barr += "-"*total
    return barr

main()
