"""CoPrimeV1"""

def main():
    """CoPrimeV1"""
    lst_num = []
    for _ in range(5):
        lst_num.append(int(input()))
    lst_num.sort()
    for i in lst_num:
        print(i)

main()
