"""Black_Canyon"""

def main():
    """main"""
    pay1 = my_f()
    pay2 = my_f()
    pay3 = my_f()
    pay4 = my_f()
    pay5 = my_f()
    total = float(pay5+pay4+pay3+pay2+pay1)
    print("Total : %.2f Baht" %total)

def my_f():
    """my_function"""
    drink = int(input())
    cake = int(input())
    pay = ((drink+cake)-((drink+cake)*0.2))-((drink+cake)-((drink+cake)*0.2))*0.1
    return pay

main()
