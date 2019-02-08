#include <stdio.h>
#include <ctype.h>

int main()
{
    char var;
    scanf("%c", &var);
    if (isdigit(var))
        printf("number\n");
    else{
        if (islower(var))
            printf("lowercase\n");
        else{
            if (isupper(var))
                printf("uppercase\n");
            else
                printf("error\n");
        }
    }
    return 0;
}