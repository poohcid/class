/*ee*/
#include<stdio.h>
main()
{
	int N,M,E,I;
N=2;
	printf("input ");
	scanf("%d",&M);
	while (N<=M)
	{ E=2;
			while (E<=N)
	  {
	  	I=(N%E);
	  	
	  	if (I==0){
	  		if (N==E){
	  			printf("%d ",N);
	  			E++;
			  }else {
			  	
			  }
		  }else {
		  	E++;
		  }
	  }  N++;
    }
       printf(".");
		
	getch();
}
