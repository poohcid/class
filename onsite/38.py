"""table I"""

def main():
    """print Multiplication table of 15"""
    count = int(input()) #many Multiplication
    for i in range(1, count+1):
        print("15 x %d = %d" %(i, 15*i))

main()
