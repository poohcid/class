"""psit"""
import json

def main():
    """psit"""
    items = json.loads(input())
    wanted = float(input())
    for i in dict(items):
        if wanted > int(items[i]):
            items.pop(i)
    if len(items) == 0:
        print("Nope")
    else:
        word = [i for i in items]
        word.sort()
        for i in word:
            print("%s\t%.2f" %(i, items.get(i)))

main()
