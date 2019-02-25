#include <stdio.h>

int main()
{
    char text[21];
    int lp0, lp1, count0=0, count1=0, check;
    scanf("%d %s", &lp0, text);
    lp1 = lp0;
    check = text[0];
    for (int i=0; text[i] != '\0'; i++){
        if (text[i]%2 == 0){
            lp1--, count1=0;
            if (text[i] == check)
                count0++;
            else
                check = text[i], count0=1;
        }
        else{
            lp0--, count0=0;
            if (text[i] == check)
                count1++;
            else
                check = text[i], count1=1;
        }
        if (count0 == 3)
            lp1 -= 3, count0=0;
        if (count1 == 3)
            lp0 -= 3, count1=0;
    }
    if (lp0 == lp1)
        printf("- ");
    else
        lp0 > lp1 ? printf("0 "):printf("1 ");
    printf("%d %d\n", lp0, lp1);
    return 0;
}