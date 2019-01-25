"""Even_Odd"""

def main():
    """Function_input_"""
    kang1, dist1 = int(input()), int(input())
    kang2, dist2 = int(input()), int(input())
    if dist1 > dist2:
        while True:
            if kang1 == kang2:
                print("YES")
                break
            elif kang1 > kang2:
                print("NO")
                break
            kang1 += dist1
            kang2 += dist2
    else:
        print("NO")

main()
