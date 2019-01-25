"""FirstROR"""

def main():
    """Function_input_"""
    text = input()
    if ("ror" in text) and ("first" in text) and ("mak" in text):
        print("P'First ror mak mak!!")
    elif ("ror" in text or "first" in text) and "mak" in text:
        print("I think so!!")
    elif ("first" in text) and ("ror" in text):
        print("I'm so First!!")
    else:
        print("First == ror -> is always True!!")

main()
