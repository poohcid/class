#include <stdio.h>

int main()
{
    double var1, var2;
    scanf("%lf %lf", &var1, &var2);
    printf("Perimeter of rectangle = %.4lf units\n", 2*(var1+var2));
    return 0;
}