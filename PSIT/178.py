"""OneTwo"""

def main():
    """OneTwo"""
    lst_onetwo = ["1", "2"]
    count = int(input())
    for _ in range(3, count+1):
        lst_onetwo.append(lst_onetwo[-1]+lst_onetwo[-2])
    print(lst_onetwo[-1] if count >= 2 else "1")

main()
