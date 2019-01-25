"""Bon Appetit"""

def main():
    """Function_input_"""
    chilli = int(input())
    level = input()
    many = int(input())
    if level == "MILD" and (1000*many) <= chilli:
        print("Enough\n%d" %(chilli-(1000*many)))
    elif level == "MEDIUM" and (2000*many) <= chilli:
        print("Enough\n%d" %(chilli-(2000*many)))
    elif level == "SPICY" and (3000*many) <= chilli:
        print("Enough\n%d" %(chilli-(3000*many)))
    else:
        print("Not Enough")

main()
