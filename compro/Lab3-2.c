#include <stdio.h>

int main()
{
    float sum=0.0, number, average;
    scanf("%f", &number);
    sum += number;
    scanf("%f", &number);
    sum += number;
    scanf("%f", &number);
    sum += number;
    scanf("%f", &number);
    sum += number;
    printf("Summation is %.2f\n", sum);
    average = sum/4;
    printf("Average is %.3f\n", average);
    return 0;
}