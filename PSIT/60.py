"""Blackjack"""

def main():
    """print 1 - count for count time"""
    count = int(input())
    score = 0
    ace = 0
    for _ in range(count):
        card = input()
        if card.isalpha():
            if card == "A":
                score += 11
                ace += 1
            else:
                score += 10
        else:
            score += int(card)
        while (ace > 0) and (score > 21):
            score -= 10
            ace -= 1
    print(score)

main()
