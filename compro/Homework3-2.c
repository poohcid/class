#include <stdio.h>

int main()
{
    int many, price;
    float per;
    scanf("%d %f %d", &price, &per, &many);
    printf("%.2f\n", (price*many)*((100-per)/100));
    return 0;
}