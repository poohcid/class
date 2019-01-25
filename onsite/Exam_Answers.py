"""Exam_Answers"""

def main():
    """main"""
    text1 = input()
    text2 = input()
    count, score = 0, 0
    for text in text1:
        if text2[count] == text:
            score += 1
        count += 1
    if score == 0:
        print("Pokpak")
    else:
        print("Score : %d/%d" %(score, len(text1)))
        print("%.2f" %(score/len(text1)*100)+"%")

main()
