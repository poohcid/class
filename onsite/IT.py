"""IT"""

def main():
    """Function_input_"""
    size = int(input())
    for _ in range(size):
        print("*"*(size*3)+" "*size+"*"*(size*3))
    for _ in range(size*2):
        print(" "*size+"*"*(size)+" "*(size*3)+"*"*size)
    for _ in range(size):
        print("*"*(size*3)+" "*(size*2)+"*"*size)

main()
