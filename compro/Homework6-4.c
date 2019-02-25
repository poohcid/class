#include <stdio.h>
#include <string.h>

int main()
{
    char text[101];
    int size[20][2], i, count=-1, index=0, check=-1;
    scanf("%[^\n]", text);
    size[0][0] = 0;
    size[0][1] = 0;
    for (i = 0; i != strlen(text); i++){
        if (text[i] != ' ')
            count++;
        if (text[i] == ' '){
            size[index][1] = count;
            index++, count++;
            size[index][0] = count+1;
        }
    }
    size[index][1] = count;
    count = -1;
    for (i = 0; i < index+1; i++){
        if (size[i][1]-size[i][0]+1 > check)
            check = size[i][1]-size[i][0]+1, count++;
    }
    for (i=size[count][0]; i <= size[count][1]; i++)
        printf("%c", text[i]);
    printf("\n", check);
    return 0;
}