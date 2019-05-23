#include <stdio.h>
#include <string.h>
int main ()
{
char str[] = "This is a string";
char ch = 's';
char *result;
result = strchr(str,ch);
while(result != NULL) {
printf("Found at position: %s\n", result);
result = strchr(result+1,ch);
}
return 0;
}