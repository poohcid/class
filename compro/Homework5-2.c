#include <stdio.h>

int main()
{
    int high, count1, count2;
    scanf("%d", &high);
    for (count1=0; count1 < high; count1++){
        for (count2=0; count2 < high; count2++){
            if (count2 == count1 || count2 == (high-count1-1))
                printf("-");
            else
                printf("#");
        }
        printf("\n");
    }
    return 0;
}