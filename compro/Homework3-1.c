#include <stdio.h>

int main()
{
    int price;
    float radius, high, result;
    double pi=3.14159265359;
    scanf("%d %f %f", &price, &radius, &high);
    radius /= 2;
    result = high*pi*radius*radius;
    printf("Volume : %.2fml\n", result);
    printf("Baht/ml : %.4f\n", price/result);
    return 0;
}