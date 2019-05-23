#include <stdio.h>
#include <string.h>

int main(){
    char name1[200], name2[200];
    scanf("%s %s", name1, name2);
    int check[] = {0, 0};
    for (int i=0; check[0] != 1 || check[1] != 1; i++){
        if (name1[i] == '\0')
            check[0] = 1;
        if (name2[i] == '\0')
            check[1] = 1;
        if (check[0] == 0)
            printf("%c", name1[i]);
        if (check[1] == 0)
            printf("%c", name2[i]);
    }
    printf("\n");
    return 0;
}