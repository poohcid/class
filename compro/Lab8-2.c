#include <stdio.h>
#include <string.h>
#include <ctype.h>
struct info{
    char name[61], surname[61], sex[10], id[13];
    int age;
    float gpa;
    } man[20];
void change(int i, int j);
int main()
{
    char type[10];
    int i, j;
    for (i=0; i < 20; i++)
        scanf("%s %s %s %d %s %f", man[i].name, man[i].surname, man[i].sex, &man[i].age, man[i].id, &man[i].gpa);
    scanf("%s", type);
    for (i=0; i < strlen(type); i++)
        type[i] = tolower(type[i]);
    if (strcmp("name", type) == 0){
        for (i=0; i < 20; i++){
            for (j=i; j < 20; j++){
                if (strcmp(man[i].name, man[j].name) >= 1)
                    change(i, j);
            }
        }
    }
    if (strcmp("surname", type) == 0){
        for (i=0; i < 20; i++){
            for (j=i; j < 20; j++){
                if (strcmp(man[i].surname, man[j].surname) >= 1)
                    change(i, j);
            }
        }
    }
    if (strcmp("id", type) == 0){
        for (i=0; i < 20; i++){
            for (j=i; j < 20; j++){
                if (strcmp(man[i].id, man[j].id) >= 1)
                    change(i, j);
            }
        }
    }
    for (i=0; i < 20; i++){
        if (strcmp("Male", man[i].sex) == 0)
            printf("Mr %c %s (%d) ID: %s GPA %.2f\n", man[i].name[0], man[i].surname, man[i].age, man[i].id, man[i].gpa);
        else
            printf("Miss %c %s (%d) ID: %s GPA %.2f\n", man[i].name[0], man[i].surname, man[i].age, man[i].id, man[i].gpa);
    }
    return 0;
}

void change(int i, int j){
    char bname[61], bsex[10], bid[13];
    int bage;
    float bgpa;
    strcpy(bname, man[j].name);
    strcpy(man[j].name, man[i].name);
    strcpy(man[i].name, bname);

    strcpy(bname, man[j].surname);
    strcpy(man[j].surname, man[i].surname);
    strcpy(man[i].surname, bname);

    strcpy(bsex, man[j].sex);
    strcpy(man[j].sex, man[i].sex);
    strcpy(man[i].sex, bsex);

    strcpy(bid, man[j].id);
    strcpy(man[j].id, man[i].id);
    strcpy(man[i].id, bid);

    bage = man[j].age;
    man[j].age = man[i].age, man[i].age = bage;

    bgpa = man[j].gpa;
    man[j].gpa = man[i].gpa, man[i].gpa = bgpa;
}