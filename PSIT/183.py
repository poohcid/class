"""Scout"""

def main():
    """Scout"""
    many = int(input())
    for _ in range(many):
        pot = []
        npq = list(map(int, input().split()))
        egg = list(map(int, input().split()))
        egg.sort()
        while 1:
            if len(egg) == 0:
                break
            if len(pot + [egg[0]]) <= npq[1] and sum(pot) + egg[0] <= npq[2]:
                pot.append(egg[0])
                del egg[0]
            else:
                break
        print(len(pot))

main()
