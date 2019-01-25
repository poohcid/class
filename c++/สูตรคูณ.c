/*poohcid rugrawi M.4/2 No.9*/
#include<stdio.h>
main()
{
      int NUMBER,N,F;
      loop:
      printf("\n\nEnter number of multiply : ");
      scanf("%d",&NUMBER);
      printf("\n\nEnter number : ");
      scanf("%d",&F);
      for (N=1;N<=F;N++)
      printf("\n%dx%d=%d",NUMBER,N,NUMBER*N);goto loop;
      getch();
      }
