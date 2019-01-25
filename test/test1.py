"""Classify"""
def main():
    """First time using dict"""
    check = 0
    student = {}
    while 1:
        num = input()
        if num == "END":
            break
        else:
            if num[:4] not in student:
                student[num[:4]] = 1
            else:
                student[num[:4]] += 1
    student_sort = dict(sorted(student.items()))
    for key in student_sort:
        if key[:2] != check:
            print(key[:2], int(key[2:4]), student_sort[key])
            check = key[:2]
        else:
            print("--", int(key[2:4]), student_sort[key])
main()
