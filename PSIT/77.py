"""FourDirections"""

def main():
    """ชี้ลูกศร"""
    text = input()
    total = ""
    for i in range(1, 6):
        for j in text:
            if j in "U":
                total += up_and_down(i, j)
            elif j in "D":
                total += up_and_down(i, j)
            elif j in "L":
                total += left_rigth(i, j)
            elif j in "R":
                total += left_rigth(i, j)
        print(total)
        total = ""

def up_and_down(count, style):
    """upper"""
    text = ""
    if (count == 1 and style == "U") or (count == 5 and style == "D"):
        text = "  *   "
    elif (count == 2 and style == "U") or (count == 4 and style == "D"):
        text = " ***  "
    elif count == 3:
        text = "* * * "
    elif (4 <= count <= 5 and style == "U") or (2 >= count >= 1 and style == "D"):
        text = "  *   "
    return text

def left_rigth(count, style):
    """down"""
    text = ""
    if count == 1 or count == 5:
        text = "  *   "
    elif style == "L" and (count == 2 or count == 4):
        text = " *    "
    elif style == "R" and (count == 2 or count == 4):
        text = "   *  "
    elif count == 3:
        text = "***** "
    return text

main()
