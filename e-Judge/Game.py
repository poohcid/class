"""Game"""

def main():
    """Function_input_"""
    money = int(input())
    if money >= 2100:
        print("Detroit: Become Human")
        money = money-2100
    if money >= 1499:
        print("Grand Theft Auto V")
        money = money - 1499
    if money >= 1399:
        print("Overwatch")
        money = money - 1399
    if money >= 945:
        print("Minecraft: Java Edition")
        money = money - 945
    if money >= 315:
        print("Stardew Valley")

main()
