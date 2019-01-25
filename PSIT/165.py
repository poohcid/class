"""Brick Bridge"""

def main():
    """Brick Bridge"""
    brick_a, brick_b = int(input()), int(input())
    goal = int(input())
    want_b = goal//5
    goal -= 5*min(want_b, brick_b)
    if brick_a >= goal:
        print(goal)
    else:
        print(-1)

main()
