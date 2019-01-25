/*Noppadon Watchalachaitrakul M.4/2 No.20*/
#include<stdio.h>
main()
{
      int x,n=1,y=1;
      printf("Enter square : ");
      scanf("%d",&x);
      while (n<=x)
      {
       while (y<=x){
	   printf("*");
       y++;
       }
      printf("\n");
      n++;
      }
      getch();
      }
