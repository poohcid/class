"""ValidVar"""

def main():
    """ValidVar"""
    count = int(input())
    for _ in range(count):
        var = input().strip()
        check = 1
        for i in var:
            if var in ["if", "else", "elif", "while", "for", "True", "False", \
            "continue", "break", "return", "is", "in", "and", "or", "from", \
            "as", "not", "def", "None", "pass"]:
                check = 0
                break
            elif var[0].isdigit():
                check = 0
                break
            elif not (i.isalpha() or i == "_" or i.isdigit()):
                check = 0
                break
        print("Valid" if check else "Invalid")

main()
