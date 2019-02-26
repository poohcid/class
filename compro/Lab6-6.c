#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char list_name[20][61], name[61], name2[61];
    int i, j, k, count, check;
    for (i=-1; i < 19; i++){
        count=0;
        scanf(" %[^\n]", name);
        check=0;
        for (j=0; j <= i; j++){
            strcpy(name2, list_name[j]);
            for (k=0; name[k] != '\0' || name2[k] != '\0'; k++){
                if (tolower(name[k]) < tolower(name2[k])){
                    check=1;
                    break;
                }
                if (tolower(name[k]) > tolower(name2[k])){
                    count++;
                    break;
                }
            }
            if (check == 1)
                break;
        }
        //sort state
        for (j=i; count <= j; j--)
            strcpy(list_name[j+1], list_name[j]);
        strcpy(list_name[count], name);
    }
    for (i=0; i < 20; i++){
        for (j=0; j < strlen(list_name[i]); j++){
            if (j == 0 || list_name[i][j-1] == ' ')
                printf("%c", toupper(list_name[i][j]));
            else
                printf("%c", tolower(list_name[i][j]));
        }
        printf("\n");
    }
    return 0;
}