"""ppap"""

def main():
    """print_DNA"""
    score = 0
    while True:
        if input() == "Pen":
            score += 1
        else:
            print("Wrong lyrics!")
            score = 0
            continue
        score = lyrics("Pineapple", score)
        if score == 0:
            continue
        score = lyrics("Apple", score)
        if score == 0:
            continue
        score = lyrics("Pen", score)
        if score == 0:
            continue
        if score == 4:
            print("Correct lyrics!")
            break

def lyrics(text, score):
    """score_text"""
    text2 = input()
    if (text2 == text) or (text2 == "Pen"):
        if (text2 == "Pen") and (text != "Pen"):
            print("Wrong lyrics!")
            score += 1
        else:
            score += 1
    else:
        print("Wrong lyrics!")
        score = 0
    return score

main()
