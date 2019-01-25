"""Alphabet"""

def main(text, add):
    """Function_input_"""
    for count in range(65, 91):
        print(chr(count), end="")
        if count == ord(text):
            add = 1
            break
    if add == 0:
        for count in range(97, 123):
            print(chr(count), end="")
            if count == ord(text):
                break

main(input(), 0)
