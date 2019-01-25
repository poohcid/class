"""BookWorm"""

def main():
    """BookWorm"""
    for _ in range(int(input())):
        worm = int(input())
        book = int(input())
        lst_book = sorted([float(input()) for _ in range(book)])
        total = []
        for i in lst_book:
            if i + sum(total) <= worm:
                total.append(i)
        print(len(total))

main()
