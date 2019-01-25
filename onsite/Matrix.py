"""Matrix"""

def main():
    """main"""
    high, wide = int(input()), int(input())
    text1, text2 = [], []
    for _ in range(high):
        for _ in range(wide):
            text2.append(int(input()))
        text1.append(text2)
        text2 = []
    for i in text1:
        print(*i) #del []

main()
