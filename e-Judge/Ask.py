"""Grade"""

def main():
    """Function_input_"""
    number = int(input())
    if number >= 1:
        if number >= 4:
            if number >= 8:
                print("Extremely Happy")
            else:
                print("Very Happy")
        else:
            print("Happy")
    else:
        print("Sad")

main()
