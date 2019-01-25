"""SUM"""

def main():
    """main"""
    count, total = int(input()), 0
    for around in range(1, count+1):
        number = 1
        if around > 1:
            print(1, end=" ")
            for i in range(1, around):
                print("+", end=" ")
                print(i+1, end=" ")
                number += i+1
        else:
            print("1", end=" ")
        print("= %d" %number)
        total += number
    print("SUM: %d" %total)

main()
