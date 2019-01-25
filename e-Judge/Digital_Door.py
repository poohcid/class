"""Digital_Door"""

def main():
    """function_main"""
    total = 0
    score = 0
    while True:
        code = input()
        if code == '-1':
            break
        if code == 'S':
            score = 1
        if code == 'E' and score == 1:
            total += 1
            score = 0
    print(total)

main()
