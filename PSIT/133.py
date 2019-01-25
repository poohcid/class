"""VerticalHistogram"""

def main(text):
    """VerticalHistogram"""
    lst_char, lst_many = list(set(text)), list(set(text))
    lst_char.sort(key=str.swapcase)
    lst_many.sort(key=text.count)
    for i in range(text.count(lst_many[-1]), 0, -1):
        print("%03d " %i, end="")
        for j in lst_char:
            print("* " if text.count(j) >= i else "  ", end="")
        print()
    print("   ", *lst_char)

main(input())
