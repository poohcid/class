#include <stdio.h>

int main()
{
    int word[26][2], count, index=-1, check=1, j, i;
    char name, name2;
    scanf("%d", &count);
    for (i=0; i < count; i++){
        scanf(" %c", &name);
        name2 = (name >= 95)?name-32:name+32;
        for (j=0; j <= index; j++){
            if (name == word[j][0] || name2 == word[j][0])
                word[j][1]++, check=0;
        }
        if (check == 1){
            name = (name <= 90)?name2:name;
            word[++index][0] = name;
            word[index][1] = 1;
        }
        check = 1;
    }
    for (i=0; i <= index; i++)
        printf("%c: %d\n", word[i][0], word[i][1]);
    printf("\n");
    return 0;
}