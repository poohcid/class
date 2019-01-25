"""End_of_the_world"""

def main():
    """function_main"""
    name = input()
    devil = int(input())
    man = int(input())
    total1 = devil
    if man > (devil*0.3):
        total1 = devil-(devil*0.45)
    if "Justify yourself!" == name:
        total1 = total1-(total1*0.2)
    devil = total1
    devil = devil - man
    if devil <= 0:
        print("We saved the world!")
    elif devil > 1000:
        print("End of the world.")
    else:
        print("A great loss.")

main()
