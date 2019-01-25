"""Mysterious"""

def main():
    """function_main"""
    stand = float(input())
    while True:
        number = float(input())
        if number < stand:
            print("More!")
        elif number > stand:
            print("Too Much!")
        else:
            break
    print("Yeah!")

main()
