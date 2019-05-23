#include <stdio.h>
#include <string.h>

int main(){
    struct records{
        int money, com;
        char name[200], id[20];
    };
    char search[20];
    int count, check=0;
    scanf("%d", &count);
    struct records info[count];
    for (int i=0; i < count; i++)
        scanf("%s %s %d %d", info[i].id, info[i].name, &info[i].money, &info[i].com);
    scanf("%s", search);
    for (int i=0; i < count; i++){
        if (strcmp(info[i].id, search) == 0){
            printf("%s\n%s\n%d\n%.2f\n%d\n%.2f\n", info[i].id, info[i].name, info[i].com, (info[i].com*0.02), info[i].money, (info[i].com*0.02+info[i].money));
            check = 1;
        }
    }
    if (check == 0)
        printf("ID not found !!!\n");
    return 0;
}