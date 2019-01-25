"""FoodGrade I"""

def main():
    """Function process and print"""
    total = size()+size()+size()+size()+size()+size()
    print(total)

def size():
    """return total"""
    total = want(int(input()), int(input()))
    total += want(int(input()), int(input()))
    return total

def want(size1, size2):
    """return want to be"""
    total = 0
    if 50 <= size1 <= 70:
        total += 1
    if 50 <= size2 <= 70:
        total += 1
    return total

main()
