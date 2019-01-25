/*677*/
#include<stdio.h>
main()
{
	int e=2,n=0;
	float o=0;
	printf("\nin put: ");
	scanf("%d",&n);
	if (n==1){
		printf("no");
	}else {
	
	while (e<n)
	  {
	  	o=(n%e);
	  	
	  	if (o==0){
	  		if (n==2){
	  			printf("yes\n%d",e);break;
			  }else {
			  	printf("no\n%d",e);break;
			  }
		  }else {
		  	e++;
		  }
	  }
	  if (e<n){
	  	printf(".");
         }else{
		 
	  printf("yes\n %d",e);
	  }
}
     getch();
     
}



