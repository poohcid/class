"""Sleepy"""

def main():
    """Function_main_"""
    total = my_f1(1)+'\n'+my_f1(2)+'\n'+\
    my_f1(3)+'\n'+my_f1(4)+'\n'+\
    my_f1(5)+'\n'+my_f1(6)+'\n'+\
    my_f1(7)+'\n'+my_f1(8)+'\n'+\
    my_f1(9)+'\n'+my_f1(10)
    print(total)

def my_f1(day):
    """print_function"""
    hour = int(input())
    minu = int(input())
    lazy = int(input())
    wake = ("%02d:%02d" %(hour, minu))
    many = my_f2(lazy)
    hourf = many//60
    minuf = many%60
    hour = (60 <= (minu+minuf))+hourf+hour
    minu = ((minu+minuf)%60)
    finish = ("%02d:%02d" %(hour, minu))
    total = ("[Day %02d] %s - %s (Time Used: %d Hour(s) %d Minute(s))"\
    %(day, wake, finish, hourf, minuf))
    return total

def my_f2(lazy):
    """lazy_function"""
    total = (10+(lazy))+(40+5*(lazy))+15
    return total

main()
