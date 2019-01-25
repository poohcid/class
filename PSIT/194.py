"""Heads and Legs"""

def main():
    """Heads and Legs"""
    many, legs = int(input()), int(input())
    bird = (legs - 4*(many))/(-2)
    bunny = many - bird
    if bird == int(bird) and bunny == int(bunny) and bunny >= 0 and bird >= 0:
        print(int(bunny), int(bird))
    else:
        print("Impossible")
main()
