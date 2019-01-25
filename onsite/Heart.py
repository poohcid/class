"""Heart"""

def main(size):
    """Function_input_"""
    line = 1
    line2 = 1+(size-2)*2
    print(" "*(size-1)+"*"+" "*line2+"*")
    line1 = size-2
    line2 -= 2
    for i in range(1, 1+(size-2)*2, 2):
        print(" "*line1+"*"+"-"*i+"*"+" "*line2+"*"+"-"*i+"*")
        line1 -= 1
        line2 -= 2
        line = i
    line += 2*(size > 2)
    print("*"+"-"*line+"*"+"-"*line+"*")
    line = line*2-1
    line1 = 1
    for i in range(line, 0, -2):
        print(" "*line1+"*"+"-"*i+"*")
        line1 += 1
    print(" "*line1+"*")

main(int(input()))
