/*poohcid rugrawi M.4/2 No.9*/
#include<stdio.h>
main()
{
      int N,NUMBER,X;
      float sum=1,avg=0;
      float U;
      printf("\nEnter number of multiply : ");
      scanf("%d",&N);
      for (X=0,NUMBER=1;NUMBER<=N;NUMBER++)
      
      printf("\nEnter number%d:%d",NUMBER,NUMBER);
      X+=NUMBER;
      U=(X/N);
      printf("\naverage is %.2f",U);

      getch();
      }
