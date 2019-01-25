"""BreachTheDoor"""

def main():
    """BreachTheDoor"""
    text = input().split()
    for i in text:
        if len(i) > 6:
            while not i[-1].isalpha():
                i = i.rstrip(i[-1])
                if len(i) == 0:
                    break
            if len(i) > 6:
                print(i, end=" ")

main()
