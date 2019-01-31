#include <stdio.h>

int main()
{
    int sec, day, hour, minu, times;
    scanf("%d", &times);
    sec = times;
    day = sec/86400;
    sec %= 86400;
    hour = sec/3600;
    sec %= 3600;
    minu = sec/60;
    sec %= 60;
    printf("%d s = %d d %d h %d m %d s \n", times, day, hour, minu, sec);
    return 0;
}