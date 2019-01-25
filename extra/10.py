"""Hidden Message"""

def main():
    """main"""
    name, text = input(), input()
    if name == "Monday":
        count = 2
    elif name == "Tuesday":
        count = 3
    elif name == "Wednesday":
        count = 4
    elif name == "Thursday":
        count = 5
    elif name == "Friday":
        count = 6
    elif name == "Saturday":
        count = 7
    elif name == "Sunday":
        count = 8
    for i in range(count-1, len(text)+1, count):
        print(text[i], end="")

main()
