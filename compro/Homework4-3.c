#include <stdio.h>

int main()
{
    int many, per;
    float price, total1, total2;
    scanf("%f %d %d", &price, &per, &many);
    total1 = price*many*((100-per)/100.0);
    total2 = price*(many*2/3) + price*(many%3);
    total1 <= total2 ? printf("Discount %d%%\n%.2f\n", per, total1) : printf("Buy 2 Get 1\n%.2f\n", total2);
    return 0;
}