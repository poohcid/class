#include <stdio.h>
#include <math.h>

int main()
{
    double var1, var2;
    scanf("%lf,%lf", &var1, &var2);
    printf("The sum of the given numbers : %lf\n", var1+var2);
    printf("The difference of the given numbers : %lf\n", var1-var2);
    printf("The product of the given numbers : %lf\n", var1*var2);
    printf("The quotient of the given numbers : %lf\n", var1/var2);
    return 0;
}