/*poohcid rugrawi M.4/2 N0.9*/
#include<stdio.h>
main()
{
	int x,z,n,o,q;
	float ;
	char y;
	printf("enter number(1) : ");
	scanf("%d",&x);
	printf("enter proscec : ");
	scanf("%s",&y);
	switch(y){
		case '+':printf("enter number(2) : ");
		scanf("%d",&z);
		o=x+z;
		printf("                 =%d",o);break;
		case '-':printf("enter number(2) : ");
		scanf("%d",&z);
		o=x-z;
		printf("                 =%d",o);break;
        case '*':printf("enter number(2) : ");
		scanf("%d",&z);
		o=x*z;
		printf("                 =%d",o);break;
		case '/':printf("enter number(2) : ");
		scanf("%d",&z);
		q=x/z;
		printf("                 =%d",q);break;
		case '%':printf("enter number(2) : ");
		scanf("%d",&z);
		q=x%z;
		printf("%d",q);break;
		default:for(n==1;n<=x;n++)
		printf("\t*");
	}
	getch();
}
