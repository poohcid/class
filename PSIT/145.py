"""PedPonFire"""

def main():
    """PedPonFire"""
    count = int(input())
    duck1 = [int(input()) for _ in range(count)]
    duck2 = sorted(set(duck1))
    gass = int(input())
    duck1.sort()
    total = 0
    for i in duck2:
        if i > gass/2:
            break
        if gass - i in duck1:
            total += duck1.count(gass - i)*duck1.count(i)
    print(total)

main()
