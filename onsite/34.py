"""Stepper II"""

def main():
    """print start number to stop number"""
    number = int(input())
    stop = int(input())+1
    step = 1
    if number > stop: #revers count
        step = -1
        stop -= 2
    for i in range(number, stop, step):
        print(i)
main()
