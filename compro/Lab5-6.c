#include <stdio.h>

int main()
{
    double max_var, min_var, number, total=0;
    int many;
    scanf("%d", &many);
    scanf("%lf", &max_var);
    min_var = max_var;
    total += max_var;
    many--;
    for (int count=0; count < many; count++){
        scanf("%lf", &number);
        if (number >= max_var){
            if (count == 0)
                min_var = max_var;
            max_var = number;
        }
        else if (number < min_var){
            if (count == 0)
                max_var = min_var;
            min_var = number;
        }
        total += number;
    }
    printf("%d Values\n", many+1);
    printf("Min: %.3lf\n", min_var);
    printf("Max: %.3lf\n", max_var);
    printf("Avg: %.2lf\n", total/(many+1));
    return 0;
}