#include <stdio.h>

int main()
{
    float score;
    scanf("%f", &score);
    if (100 >= score && score >= 80)
        printf("A");
    if (80 > score && score >= 70)
        printf("B");
    if (70 > score && score >= 60)
        printf("C");
    if (60 > score && score >= 50)
        printf("D");
    if (50 > score && score >= 0)
        printf("F");
    if (score > 100 || score < 0)
        printf("Out of Range");
    printf("\n");
    return 0;
}