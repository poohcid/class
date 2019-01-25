"""Admission"""

def main():
    """function_main"""
    score = int(input())
    fac1 = input()
    fac2 = input()
    fac3 = input()
    fac4 = input()
    if fac1 in rank(score, fac1):
        print(fac1)
    elif fac2 in rank(score, fac2):
        print(fac2)
    elif fac3 in rank(score, fac3):
        print(fac3)
    elif fac4 in rank(score, fac4):
        print(fac4)
    else:
        print("None")

def rank(score, fac):
    """consider"""
    if "A" in fac and score >= 20000:
        con = "A"
    elif "B" in fac and score >= 17500:
        con = "B"
    elif "C" in fac and score >= 18000:
        con = "C"
    elif "D" in fac and score >= 28250:
        con = "D"
    elif "E" in fac and score >= 27000:
        con = "E"
    elif "F" in fac and score >= 25000:
        con = "F"
    elif "G" in fac and score >= 21750:
        con = "G"
    elif "H" in fac and score >= 22000:
        con = "H"
    else:
        con = "T^T"
    return con

main()
