#include <stdio.h>
main()
{
	int I,num1,num2,num3,num4,e;
	printf("input: ");
	scanf("%d",&I);
	num1=0; num2=1; num3=0; num4=0;
	for (e=1;I>=e;e++)
	{
		printf("%d ",num1);
		num4=(num1+num2);
		num3=(num2);
		num1=(num3);
		num2=(num4);
	}
}
