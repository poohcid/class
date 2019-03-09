#include <stdio.h>

long long fac(int number);
int coinBoot(int coin, int type, int use);
int LIST[] = {0, 0, 2, 0, 0, 2, 0, 0, 0, 5, 2};

int main()
{
    int coin, count=0;
    scanf("%d", &coin);
    count += (coin >= 10)?coinBoot(coin, 10, coin) + coinBoot(coin, 9, coin): 0;
    count += (coin >= 5)?coinBoot(coin, 5, coin) : 0;
    count += (coin >= 2)?coinBoot(coin, 2, coin) : 0;
    printf("%d\n", count);
}

long long fac(int number){
    long long int total=1;
    for (int i=number; i > 0; i--)
        total *= i;
    return total;
}

int coinBoot(int coin, int type, int use){
    long total=1;
    if (type == 2){
        for (int i=1; i < (use/type + use%type); i++)
            total += coin/(fac(i)*fac(use-i-i));
        total += (coin%2==0 && type==2) + coin*(coin%2==0 && type!=2);
        return total;
    }
    else{
        for (int i=1; i <= (coin/(type+(type == 9))); i++)
            total += coinBoot(coin-type+1, LIST[type], coin-(i*type))/fac(i);
    }
    return total+(coin-type)*(coin/type > 1);
}
