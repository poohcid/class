"""Service"""

def main():
    """function"""
    pay = int(input())
    total = int(((pay+(pay*0.1))*0.07)+(pay+(pay*0.1)))
    print(total)
main()
