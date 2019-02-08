#include <stdio.h>

int main()
{
    char var;
    scanf("%c", &var);
    if (var >= 65 && var <= 90)
        printf("%c\n", var+32);
    else if (var >= 97 && var <= 122)
        printf("%c\n", var-32);
    else
        printf("error\n");
    return 0;
}