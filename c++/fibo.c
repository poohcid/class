#include<stdio.h>
main()
{
	int num1,num2,num3,num4,e,n;
	II:
	printf("\nin ");
	scanf("%d",&n);
	(num1)=0;   (num2)=1;   (num3)=0;   (num4)=0;  (e)=3;
	if (n<3){
		if (n==1){
			printf("___%d___",num1);
		}
	else {
		printf("___%d___",num2);
	}
}
   while (e<=n){
	num4=(num1+num2);
	num3=(num2);
	num1=(num3);
	num2=(num4);
	e++;
}
if (n<3){
	printf(" ");
}else{
	printf("___%d___",num2);
} printf("\n"); goto II;
}
