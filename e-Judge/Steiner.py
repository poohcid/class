"""Steiner"""

def main():
    """main"""
    num = float(input())
    return num

def my_f1():
    num1 = float(input())
    num2 = float(input())
    total = num1+num2
    print("%.6f" %total)
    return total

def my_f2():
    """my_f2"""
    total = my_f1()+main()
    print("%.6f" %total)
    my_f4(total)

def my_f4(x):
    """my_f4"""
    total = x+main()
    print("%.6f" %total)
    my_f4(total)

my_f2()
