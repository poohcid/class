"""Count_Fast!"""

def main():
    """main"""
    name = str(my_f(1))+'\n'+str(my_f(6))+'\n'+str(my_f(11))+'\n'+\
    str(my_f(16))+'\n'+str(my_f(21))+'\n'+\
    str(my_f(26))+'\n'+str(my_f(31))+'\n'+\
    str(my_f(36))+'\n'+str(my_f(41))+'\n'+str(my_f(46))
    print(name)

def my_f(num):
    """my_function"""
    int(num)
    name1 = input()
    name2 = input()
    name3 = input()
    name4 = input()
    name5 = input()
    total = name1+':'+str(num)+'#'+'\t\t'+name2+':'+str(num+1)+'#'+'\t\t'+\
    name3+':'+str(num+2)+'#'+'\t\t'+name4+':'+str(num+3)+'#'+'\t\t'+\
    name5+':'+str(num+4)+'#'
    return total

main()
