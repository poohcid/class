#include <stdio.h>
#include <math.h>

int main()
{
    double var1, var2, result;
    scanf("%lf %lf", &var1, &var2);
    result = var1*var1 + var2*var2;
    result = sqrt (result);
    printf("%.2lf\n", result);
    return 0;
}