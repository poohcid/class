"""psit"""

def main():
    """psit"""
    card = []
    for i in "SHDC":
        card1 = [str(j)+i for j in range(2, 11)]
        card2 = [j+i for j in "AKQJ"]
        card += card1+card2
    for _ in range(51):
        card.remove(input())
    print(*card)

main()
