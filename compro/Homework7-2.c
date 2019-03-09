#include <stdio.h>
#include <string.h>



int main()
{
    char name1[100], name2[100], buff[100];
    int count;
    scanf("%s %s %d", name1, name2, &count);
    for (int i=1; i<count; i++){
        strcpy(buff, name1);
        strcpy(name1, name2);
        strcat(buff, name2);
        strcpy(name2, buff);
    }
    printf("%s\n", name1);
    return 0;
}
