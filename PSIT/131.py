"""RemoveTag"""

def main(text):
    """RemoveTag"""
    total, gate = "", "open"
    for i in text:
        if i == "<":
            gate = "close"
            total += " "
        elif i == ">":
            gate = "open"
        elif gate == "open":
            total += i
    print(total.split())

main(input())
