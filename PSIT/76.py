"""RockPaperScissor"""

def main():
    """ใครจะชนะ"""
    text = input()
    action, score_a, score_b = "", 0, 0
    for i in text:
        if len(action) != 2:
            action += i
        if len(action) == 2:
            score_a += action.count("SP") + action.count("PR") + action.count("RS")
            score_b += action.count("PS") + action.count("RP") + action.count("SR")
            action = ""
    if score_a == score_b:
        print("DRAW", score_a)
    elif score_a > score_b:
        print("A win %d-%d" %(score_a, score_b))
    else:
        print("B win %d-%d" %(score_b, score_a))

main()
