#include <stdio.h>

int main()
{
    char name1[31], name2[31];
    int day, mouth, year, id;
    float gpa;
    scanf("%s", &name1);
    scanf("%s", &name2);
    scanf("%d", &id);
    scanf("%d/%d/%d", &day, &mouth, &year);
    scanf("%f", &gpa);
    printf("Fullname: %s %s\n", name1, name2);
    printf("ID: %d\n", id);
    printf("DOB: %02d-%02d-%02d\n", day, mouth, year);
    printf("GPA: %.2f\n", gpa);
    return 0;
}