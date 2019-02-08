#include <stdio.h>

int main()
{
    int line1, line2, line3, count=0;
    scanf("%d %d %d", &line1, &line2, &line3);
    if (line1 + line2 > line3)
        count++;
    if (line1 + line3 > line2)
        count++;
    if (line2 + line3 > line1)
        count++;
    count == 3 ? printf("Triangle is valid.\n") : printf("Triangle is not valid.\n");
    return 0;
}