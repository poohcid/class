"""Refrigerator"""

def main():
    """Refrigerator"""
    items = list(map(int, input().split()))
    count = 0
    while 0 not in items:
        count += 1
        item = min(items)
        box = items.index(item)
        del items[box]
        items = list(map(lambda x: x-1, items))
        items.insert(box, item)
        #print(items)
    print(count)

main()
