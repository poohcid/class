"""print_DNA"""

def main():
    """Function_input_"""
    size = int(input())
    many = int(input())
    for _ in range(many):
        size_dna(size)

def size_dna(size):
    """print_DNA"""
    space, line = 0, size-2
    for _ in range(size//2):
        print(" "*space+"\\"+"-"*line+"/")
        space += 1
        line -= 2
    if (size%2) > 0:
        print(" "*space+"\\")
        line += 2
        space -= 1
    else:
        space, line = (size//2)-1, 0
    for _ in range(size//2):
        print(" "*space+"/"+"-"*line+"\\")
        space -= 1
        line += 2

main()
