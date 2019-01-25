/*poohcid rugrawi M.4/2 No.9*/
#include<stdio.h>
main()
{
      int NUMBER,N=1;
      loop:printf("\n\nEnter number of multiply : ");
      scanf("%d",&NUMBER);
      while(N<=12)
      {
      printf("\n%dx%d=%d",NUMBER,N,NUMBER*N);
      N++;
      }
      goto loop;
      getch();
      }
