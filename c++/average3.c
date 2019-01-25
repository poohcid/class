/*Noppadon Watchalachaitrakul M.4/2 No.20*/
#include<stdio.h>
main()
{
      int n,number;
      float sum=0,avg;
      for(n=1;n<6;n++)
      {
      printf("Enter number %d :",n);
      scanf("%d",&number);
      sum+=number;
      }
      avg=sum/5;
      printf("Average is %.2f",avg);
      getch();
      }
