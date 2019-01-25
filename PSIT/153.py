"""WordSequence II"""

def main():
    """WordSequence II"""
    text1, text2 = input(), input()
    print(text1)
    for i in range(1, max(len(text1), len(text2)) + 1):
        print(text2[:min(len(text2), i)] + text1[i:])

main()
