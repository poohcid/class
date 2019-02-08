#include <stdio.h>

int main()
{
    double num1, num2, num3, count;
    scanf("%lf %lf %lf", &num1, &num2, &num3);
    count = num1;
    num1 = num1 < num2 ? num2 : num1, num2 = count < num2 ? count : num2;
    count = num1;
    num1 = num1 < num3 ? num3 : num1, num3 = count < num3 ? count : num3;
    count = num2;
    num2 = num2 < num3 ? num3 : num2, num3 = count < num3 ? count : num3;
    printf("%.2lf\n", num2);
    return 0;
}