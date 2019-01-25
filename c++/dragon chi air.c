/*poohcid rugrawi M.4/2 No.19*/
#include<stdio.h>
main()
{
      int PERSON,BUY,TUAR,n,t,h,th,R,ha,sa,one;
    
      printf("~~~~~~~~~~~~~~~~~~~~~~~~~~<\nWellcom to Dragon chi air\n~~~~~~~~~~~~~~~~~~~~~~~~~~<");
      printf("\ntrip: 1.the Pridsadan Island 100  2.himmapan forest 2000 3.the Moon 1000000");
      printf("\n\n\nYou want : ");
      scanf("%d",&R);
      if(R==1){
      	printf("OK A. your money: ");
      	scanf("%d",&PERSON);
      	BUY=PERSON-100;
      	if(BUY>0){
      	printf("\nI take :%d",BUY);
      	th=BUY/1000;
      	BUY=(BUY%1000);
      	printf("\nBank 1000 :%d",th);
      	h=BUY/100;
      	BUY=(BUY%100);
      	printf("\nBank 100  :%d",h);
      	t=BUY/10;
      	BUY=(BUY%10);
      	printf("\ncoin 10   :%d",t);
      	ha=BUY/5; 
      	BUY=(BUY%5);
      	printf("\ncoin 5    :%d",ha);
      	printf("\ncoin 1    :%d",BUY);
      }else{
      	printf("kuy");
	  }
		  
	  }else{
	  	printf("KUY");
	  }
	  getch();
}
      
