#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char data[] = {'Q', 'R', 'M', 'N', 'C', 'E', 'D', 'K', 'L', 'J', 'O', 'S', 'H', 'T', 'U', 'F', 'V', 'Z', 'G', 'W', 'I', 'A', 'B', 'X', 'Y', 'P'}, text[201], name;
    int index, i, j;
    scanf("%[^\n]", &text);
    for (i=0; i < strlen(text); i++){
        name = text[i];
        if (name == ' '){
            printf(" ");
            continue;
        }
        for (j=0; j < 26; j++){
            if (tolower(name) == tolower(data[j])){
                index = j;
                break;
            }
        }
        index = (index-5 < 0) ? 25+(index-5+1):index-5;
        (islower(name)) ? printf("%c", tolower(data[index])):printf("%c", data[index]);;
    }
    printf("\n");
    return 0;
}