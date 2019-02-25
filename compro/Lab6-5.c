#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char text[301], name, check=0;
    int index[300], i;
    scanf("%[^\n] ", text);
    scanf(" %c", &name);
    for (i=0; i < strlen(text); i++){
        if (tolower(name) == tolower(text[i]))
            index[check++] = i+1;
    }
    if (check >= 1){
        printf("There is/are %d \"%c\" in the above sentences.\nPosition: %d", check, name, index[0]);
        for (i=1; i < check; i++)
            printf(", %d", index[i]);
    }
    (check == 0) ? printf("Not found.\n"):printf("\n");
    return 0;
}