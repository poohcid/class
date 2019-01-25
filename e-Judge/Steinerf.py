"""Steiner"""

def main():
    """main"""
    num1 = float(input())
    toltal = my_f1(num1)
    print(toltal)

def my_f1(num1):
    """total_line"""
    toltal = (my_f3(num1))
    line = ("%.6f\n" %toltal) #1
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #2
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #3
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #4
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #5
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #6
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #7
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #8
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #9
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #10
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #11
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #12
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #13
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #14
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #15
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #16
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #17
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #18
    toltal = (my_f3(toltal))
    line = line+("%.6f\n" %toltal) #19
    toltal = (my_f3(toltal))
    line = line+("%.6f" %toltal) #20
    return line

def my_f3(num1):
    """process_line"""
    num2 = float(input())
    toltal = num1+num2
    return toltal

main()
