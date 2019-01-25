"""GCD_N"""

def main(count):
    """GCD_N"""
    number = sorted([int(input()) for _ in range(count)])
    while len(number) > 1:
        divi, result = min(number), [min(number)]
        for i in number[1::]:
            if i%divi != 0:
                result.append(i%divi)
        number = sorted([i for i in result])
    print(*number)

main(int(input()))
