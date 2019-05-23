#include <stdio.h>

int main(){
    int total=0, num;
    float result;
    printf("Number:");
    for (int i=0; i < 10; i++){
        scanf("%d", &num);
        total += num;
    }
    result = total/10.0;
    printf("%.1f\n", result);
    return 0;
}