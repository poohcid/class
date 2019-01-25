"""Steiner"""

def main():
    """main"""
    total = str(my_f1(1))+'\n'+str(my_f1(2))+'\n'+\
    str(my_f1(3))+'\n'+str(my_f1(4))+'\n'+\
    str(my_f1(5))+'\n'+str(my_f1(6))+'\n'+\
    str(my_f1(7))+'\n'+str(my_f1(8))+'\n'+\
    str(my_f1(9))+'\n'+str(my_f1(10))+'\n'+\
    str(my_f1(11))+'\n'+str(my_f1(12))+'\n'+\
    str(my_f1(13))+'\n'+str(my_f1(14))+'\n'+\
    str(my_f1(15))+'\n'+str(my_f1(16))+'\n'+\
    str(my_f1(17))+'\n'+str(my_f1(18))+'\n'+\
    str(my_f1(19))+'\n'+str(my_f1(20))
    print(total)

def my_f1(num):
    """my_f1"""
    num1 = int(input())
    num2 = float(input())
    total1 = (my_f2(num1, num2))
    total = ("Car No.%02d: %.2f Baht." %(num, total1))
    return total

def my_f2(num1, num2):
    """Process"""
    total = num1*int(num2)
    return total

main()
