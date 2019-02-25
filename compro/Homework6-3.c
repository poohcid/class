#include <stdio.h>

int main()
{
    char text1[101];
    int count=0, check=1, i;
    scanf("%s", text1);
    for (i=0; text1[i] != '\0'; i++)
        count++;
    count--;
    for (i = count; i >= 0; i--){
        if (text1[i] != text1[count-i]){
            printf("It is not Palindrome.\n");
            check = 0;
            break;
        }
    }
    if (check == 1)
        printf("It is Palindrome.\n");
    return 0;
}