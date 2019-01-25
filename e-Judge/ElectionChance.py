"""Election_Chance"""

def main():
    """function_input"""
    elec = int(input())
    year = int(input())
    year = (year-2018)
    chance = int((1-(elec/100)*year)*100)
    chance = (chance*int(chance >= 0))
    print(chance, "%")
main()
