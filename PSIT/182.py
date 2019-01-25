"""Discount"""

def main():
    """Discount"""
    lst_book = []
    book = input()
    while book.isdigit():
        lst_book.append(int(book))
        book = input()
    lst_book.sort()
    if len(lst_book) < 25:
        many = len(lst_book)
        count = (6 <= many < 12) + 2*(12 <= many < 20) + 4*(many >= 20)
        print(sum(lst_book[count:]))
    else:
        count = len(lst_book)//5
        print(sum(lst_book[count:]))

main()
