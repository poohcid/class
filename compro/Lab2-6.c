#include <stdio.h>

int main()
{
    char text[31];
    scanf("%s", &text);
    printf("String 1: %.3s\n", text);
    scanf("%s", &text);
    printf("String 1: %.4s\n", text);
    scanf("%s", &text);
    printf("String 1: %.5s\n", text);
    scanf("%s", &text);
    printf("String 1: %.6s\n", text);
    return 0;
}