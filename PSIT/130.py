"""Duplicate I"""

def main(many_1, many_2):
    """how many member in two group"""
    group_1 = [input() for _ in range(many_1)]
    total = []
    for _ in range(many_2):
        name = input()
        if name in group_1:
            total.append(name)
    total.sort(reverse=True)
    print("Nope" if len(total) == 0 else "\n".join(total))

main(int(input()), int(input()))
