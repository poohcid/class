#include <stdio.h>
#include <string.h>

int main(){
    struct info{
        char book[1000], name[1000];
        int count;
    };
    int n, m, check, index=0;
    char book1[1000], name1[1000];
    scanf("%d %d", &n, &m);
    struct info data[100];
    for (int i=0; i < m; i++){
        check = 0;
        scanf(" %[^,], %[^\n]", book1, name1);
        for (int j=0; j < index; j++){
            if ((strcmp(data[j].book, book1) == 0) && (strcmp(data[j].name, name1) == 0)){
                data[j].count++;
                check = 1;
                break;
            }
        }
        if (check == 0){
            strcpy(data[index].book, book1);
            strcpy(data[index].name, name1);
            data[index++].count = 1;
        }
    }
    if (n == 0 || index > n || m == 0){
        printf("Have no book\n");
        n = 0;
    }
    for (int i=0; i < n; i++)
        printf("%d %s, %s\n", data[i].count, data[i].book, data[i].name);
}