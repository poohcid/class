#include <stdio.h>
main()
{
loop:   int I,num1=1,num2,num3=1,M=0,f,g;
    float e;
    printf("<------function prime number ------> \n1)run number   2)position   3)check number \n\n");
    printf("select function : ");
    scanf("%d",&f);
    printf("\ninput : ");
    scanf("%d",&I);
    if (f>3){
        printf("ERROR");
    }
        if(f<=2)
        {
    while (I>=num3)
    {
        num1++; num2=2; e=1;
        while (e>0)
        {
            e=(num1%num2);
            if (e>0){
                num2++;
            }
        }
    if (num1==num2)
        {
          if (f==2){

            if (I==num3){

            printf("%d ",num1);
            } }
            if (f==1){
                printf("%d ",num1);
            }
            num3++; M++;
            if (f==1){

            if (M==5){
                printf("\n");
                M=0;
            }
            }
        }
    }
}
        if (f==3){
            num1=2;
            if (I==1){
        printf("no");
    }else {

    while (num1<I)
      {
        e=(I%num1);

        if (e==0){
            if (I==2){
                printf("yes\n2");break;
              }else {
                printf("no\n%d",num1);break;
              }
          }else {
            num1++;
          }
      } if (I>num1){
      printf(" "); }
      else{
        printf("yes \n%d",I);
      }

        }
    }
    printf("\n\nagain? press 1: ");
    scanf("%d",&g);
    if (g==1){

    printf("\n\n"); goto loop;
}
}
