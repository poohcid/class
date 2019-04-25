#include <stdio.h>
#include <string.h>
struct Weather{
    char outlook[9];
    int temp, hum;
    char wind;
};
void playing(struct Weather data2);
int main(){
    struct Weather data1;
    int days;
    scanf("%d", &days);
    for (int i=0; i<days; i++){
        scanf("%s %d %d %c", data1.outlook, &data1.temp, &data1.hum, &data1.wind);
        playing(data1);
    }
}

void playing(struct Weather data2){
    if (strcmp("overcast", data2.outlook) == 0)
        printf("yes\n");
    else if (strcmp("rain", data2.outlook) == 0){
        if (data2.wind == 'F')
            printf("yes\n");
        else
            printf("no\n");
    }
    else if (strcmp("sunny", data2.outlook) == 0){
        if (data2.hum > 77.5)
            printf("no\n");
        else
            printf("yes\n");
    }
}