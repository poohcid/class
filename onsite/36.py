"""Grade III"""

def main():
    """print GPA """
    import math
    count = int(input()) #your many subjects
    total = 0 #first total grade
    for _ in range(count):
        score = float(input())
        if 100 >= score >= 95:
            total += 4
        elif score >= 90:
            total += 3.5
        elif score >= 85:
            total += 3
        elif score >= 80:
            total += 2.5
        elif score >= 75:
            total += 2
        elif score >= 70:
            total += 1.5
        elif score >= 65:
            total += 1
        elif score >= 60:
            total += 0.5
        else:
            total += 0
    grade = math.floor((total/count)*100) # want 2nd decimal place
    grade *= 0.01 #400 --> 4.00
    print("%.2f" %grade)

main()
