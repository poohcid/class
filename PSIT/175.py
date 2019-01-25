"""MacaronBoxSML"""

def main():
    """MacaronBoxSML"""
    many = int(input())
    box_a = many//24
    many %= 24
    if many > 12:
        box_a += 1
        many = 0
    box_b = many//12
    many %= 12
    if many > 6:
        box_b += 1
        many = 0
    box_c = int(0 < many <= 6)
    print(box_c, box_b, box_a, sep="\n")

main()
