#include <stdio.h>
#include <string.h>

int main()
{
    struct info{
        char name[61], surname[61], sex[10], id[13];
        int age;
        float gpa;
    }man;
    scanf("%s %s %s %d %s %f", man.name, man.surname, man.sex, &man.age, man.id, &man.gpa);
    if (strcmp("Male", man.sex) == 0)
        printf("Mr %c %s (%d) ID: %s GPA %.2f\n", man.name[0], man.surname, man.age, man.id, man.gpa);
    else
        printf("Miss %c %s (%d) ID: %s GPA %.2f\n", man.name[0], man.surname, man.age, man.id, man.gpa);
    return 0;
}