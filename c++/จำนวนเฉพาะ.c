/*677*/
#include<stdio.h>
main()
{
	int e,n;
	float o;
	loop:
		e=2;
		n=0;
		o=0;
	printf("\n\nin put: ");
	scanf("%d)",&n);
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
}goto loop;
     getch();
}



