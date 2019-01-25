"""Dog_Tag"""

def main():
    """main"""
    name = input()
    print("/"+"-"*8+"\\")
    print("|{:^8.8s}|" .format(name))
    print("\\"+"-"*8+"/")

main()
