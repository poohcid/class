#include <stdio.h>

int main()
{
    int a = 17, b = 25, c = 50, d = 10;
    printf("%d %d %d %d\n", a, b, c, d);
    d = b % a + c / b;
    printf("%d %d %d %d\n", a, b, c, d);
    d = b % a++ + c / b;
    printf("%d %d %d %d\n", a, b, c, d);
    d = b % ++a + c / b;
    printf("%d %d %d %d\n", a, b, c, d);
    d = b % (a + c) / b;
    printf("%d %d %d %d\n", a, b, c, d);
    return 0;
}