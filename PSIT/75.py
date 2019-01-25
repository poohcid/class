"""FOR!F-Ball"""

def main():
    """slot glass"""
    text = input()
    glass = "A"
    for i in text:
        if glass == i:
            if i == "A":
                glass = "B"
            elif i == "B":
                glass = "C"
            else:
                glass = "A"
        elif glass == "B" and i == "A":
            glass = i
        elif glass == "C" and i == "B":
            glass = i
        elif glass == "A" and i == "C":
            glass = i
    print(ord(glass)-64)

main()
