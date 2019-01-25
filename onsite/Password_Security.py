"""Password Security"""

def main(count):
    """main"""
    text = input()
    if count == 1 and len(text) < 6:
        print("process terminated")
    elif len(text) < 6:
        print("try again")
        main(1)
    else:
        score = 0
        if text.isdigit():
            score += 50
        elif text.isalpha():
            score += 30
            if text.islower():
                score += 100
            elif text.isupper():
                score += 85
            else:
                score += 175
        else:
            score += 75
        if text.count(text[0]) > 3:
            score -= 15*(text.count(text[0])-3)
        if len(text) > 10:
            score += 10*(len(text)-10)
        score += ord(text[-1])
        level = "secure"*(score >= 300) + "acceptable"*( 300 > score )
        level = "poor"*(score < 150) + level*(score >= 150)
        print("Password : "+"*"*len(text))
        print("Security score : %d" %score)
        print("Security level : %s" %level)

main(0)
