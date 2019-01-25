"""Popular"""

def main():
    """function_main"""
    total = famous()+famous()+famous()+famous()+famous()
    if total == 5:
        print("Superstar")
    elif total == 4:
        print("Very Popular")
    elif total == 3:
        print("Popular")
    elif total >= 1:
        print("Ordinary Student")
    else:
        print("Invisible")

def famous():
    """input_and_level"""
    name = input()
    if "Yes" in name:
        return 1
    else:
        return 0

main()
