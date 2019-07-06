"""
penalty kick

    พี่โนชอบเตะบอลมาก และพี่โนมีความสามารถในการยิงประตูที่แม่นยำมาก โดยพี่โนจะยิงประตูไปยังจุด
    ตามพิกัดแกน x และ แกน y อย่างแม่นยำและไม่เคยผิดพลาด แต่พี่โนไม่รู้ว่าจุดในช่วงไหนถึงยิงแล้ว
    จะได้ประตูกันแน่ เพราะพี่โนบวกเลขไม่เป็น

    เขียนโปรแกรมตรวจสอบว่าตำแหน่งของลูกฟุตบอลในขณะนี้
    ถูกนับเป็นประตูหรือไม่
    ขนาดของโกลฟุตบอล จะเริ่มที่จุด a, b แล้วจะขยาย
    ความยาวตามแกนบวก ของแกน x และ แกน y
    โดยกว้าง 7.32 เมตร สูง 2.44 เมตร

    และจะรับพิกัด ตำแหน่งของลูกฟุตบอลในหน่วยสเกลเซนติเมตร!!!
    และตรงสเกลพอดี !!!!!
    *** ลูกฟุตบอลในที่นี้ จะมีขนาดเท่ากับเสาและคานพอดี ***

    ถ้ายิงแล้วเป็นประตูให้ตอบว่า GOAL GOAL GOAL
    ถ้ายิงแล้วชนคาน หรือ ชนเสา ให้ตอบว่า woodwork
    ถ้ายิงแล้วไม่ได้ประตู ให้ตอบว่า not goal

input space:
    ตำแหน่งจุด a : a จำนวนเต็ม
    ตำแหน่งจุด b : b จำนวนเต็ม
    ballแกนx: x จำนวนเต็ม
    ballแกนy: y จำนวนเต็ม >= b

"""

def main():
    """football"""
    goal_x = int(input()) + 732
    goal_y = int(input()) + 244
    ball_x = int(input())
    ball_y = int(input())
    if (ball_x not in range(goal_x-732, goal_x+1)) or (ball_y not in range(goal_y-244, goal_y+1)):
        print("not goal")
    elif (ball_x == goal_x-732 and ball_y <= goal_y) or (ball_x == goal_x and ball_y <= goal_y) or\
    (ball_x in range(goal_x-732, goal_x+1) and ball_y == goal_y):
        print("woodwork")
    else:
        print("GOAL GOAL GOAL")

main()

"""
test case

1.
    0     |  GOAL GOAL GOAL
    0     |
    130   |
    241   |

2.
    -1900     |  woodwork
    0         |
    -1169     |
    244       |

3.
    -1900     |  woodwork
    0         |
    -1167     |
    244       |

5.
    900     |  not goal
    104     |
    900     |
    350     |

6.
    900     |  GOAL GOAL GOAL
    104     |
    901     |
    347     |

7.
    900     |  GOAL GOAL GOAL
    104     |
    905     |
    248     |

8.
    900     |  woodwork
    104     |
    905     |
    348     |

9.
    -7290     |  GOAL GOAL GOAL
    104       |
    -6990     |
    104       |

10.
    -7290     |  woodwork
    104       |
    -6560     |
    104       |

11.
    -7     |  not goal
    104    |
    723    |
    349    |

12.
    -7     |  not goal
    104    |
    -8     |
    348    |


"""
