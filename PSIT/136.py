"""Safe"""

def main(text1, text2):
    """shift slot"""
    total = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            result = abs(ord(text1[i]) - ord(text2[i]))
            total += min(result, 26-result)
    print(total)

main(input(), input())
