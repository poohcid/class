"""Cards"""

def main():
    """main"""
    many = int(input())
    score, add, num1 = 0, 0, 0
    for _ in range(many):
        num2 = int(input())
        if (num1 < num2) and (add == 0):
            score += 1
        else:
            add = 1
        num1 = num2
    print(many-score)

main()
