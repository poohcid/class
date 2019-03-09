#include <stdio.h>
#include <string.h>

void change(int var1, int var2, int box1[]);
int box[] = {0, 0, 0};

int main()
{
    int i, rocation[] = {'L', 'C', 'R'};
    char start, step[31];
    scanf("%c %s", &start, step);
    (start == 'L')?box[0] = 1 : (start == 'C')?box[1] = 1: (box[2] = 1);
    for (i=0; i<strlen(step); i++)
        (step[i] == 'A')?change(0, 1, box) : (step[i] == 'B')?change(1, 2, box) : change(0, 2, box);
    for (i=0; i<3; i++)
        if (box[i] == 1) break;
    printf("%c\n", rocation[i]);
    return 0;
}

void change(int var1, int var2, int box1[]){
    int buff;
    box[0] = box1[0], box[1] = box1[1], box[2], box1[2];
    buff = box[var1];
    box[var1] = box[var2];
    box[var2] = buff;
}
