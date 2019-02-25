#include <stdio.h>

int main()
{
    int total=0, number;
    scanf("%d", &number);
    while (number != -9){
        total += number;
        scanf("%d", &number);
    }
    printf("%d\n", total);
    return 0;
}