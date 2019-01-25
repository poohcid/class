"""Pineapple"""

def main():
    """Function_input_"""
    count = 0
    while count < 4:
        text = input()
        if text == "Pen":
            if 3 > count >= 1:
                count = 1
                print("Wrong lyrics!")
                continue
            else:
                count += 1
                continue
        if (text == "Pineapple") and (count == 1):
            count += 1
            continue
        elif (text == "Apple") and (count == 2):
            count += 1
            continue
        else:
            print("Wrong lyrics!")
            count = 0
            continue
    print("Correct lyrics!")

main()
