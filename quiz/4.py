"""Contest"""

def main(sex):
    """Function"""
    if sex == "Male":
        check(["Mr.", 19, 31, 175, 55, 80, 1, 0])
    else:
        check(["Miss ", 18, 29, 160, 40, 65, 2, 1])

def check(text):
    """check order"""
    name = input()
    score = 0
    if text[1] <= int(input()) <= text[2]:
        score += 1
    if int(input()) >= text[3]:
        score += 1
    if text[4] <= int(input()) <= text[5]:
        score += 1
    if text[6] <= int(input()):
        score += 1
    if text[7] == 1:
        if input() == "No":
            score += 1
    if (score == 4 and text[0] == "Mr.") or (score == 5 and text[0] == "Miss "):
        print(text[0]+name+" passed the 1st round.")
    else:
        print(text[0]+name+" didn't pass the 1st round.")

main(input())
