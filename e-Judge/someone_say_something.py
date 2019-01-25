"""someone_say_something"""

def main():
    """Function_input_"""
    sentence = input()
    name = input()
    if name in sentence:
        print("Did someone say %s?" %name)
    else:
        print("That didn't work.")

main()
