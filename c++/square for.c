/*poohcid rugrawi M.4/2 No.9*/
#include<stdio.h>
main()
{
	int x,n,y,v,j,f,m;
	v=1;
	printf("Enter square : ");
      scanf("%d",&x);
      m=x-1;
      f=x-1;
      for(n=1;n<=x;n++)
	  {
	  	for (j=1;f>=j;j++)
	  	{
	  		printf(" ");
		  }
      	for(y=1;y<=v;y++)
		  {
      		printf("*");
		  }
      	printf("\n");
      	v=v+2;
		f=f-1;  
      }
      y=4;
      for(n=1;n<=y;n++)
      {
	  
      for(f=2;f<=m;f++)
      {
      	printf(" ");
	  }
	  printf("! !\n");
      }
      getch();
	  }
      
      
