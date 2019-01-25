"""Balloon"""

def main():
    """function_main"""
    print("P'Jack won "+won(int(input())))
    print("P'Rew won "+won(int(input())))
    print("P'Pok won "+won(int(input())))
    print("P'Fight won "+won(int(input())))
    print("P'Jub won "+won(int(input())))

def won(score):
    """score"""
    if score == 10:
        return "a large teddy bear."
    elif score >= 8:
        return "a teddy bear."
    elif score >= 6:
        return "a key chain."
    elif score >= 4:
        return "a notebook."
    elif score >= 1:
        return "a pen."
    else:
        return "nothing."

main()
