package app;

import bank.util.Account;
import bank.util.Current;
import bank.util.KYC;
import bank.util.Reccuring;
import bank.util.Savings;

public class BankDemo {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
			Account [] accounts = {
				                new Savings(1000, "Saurabh", 10000),
								new Current(1001, "Prashant", 20000, 10000),
								new Reccuring(1002, "vishal", 100000, 1000, 5)
		                      };
		((KYC)accounts[0]).linkAdhar("1111 5678 0987 6223");
		((KYC)accounts[1]).linkAdhar("1224 5178 1987 6553");

		
		for(int i=0;i<accounts.length;i++)
		{

			System.out.println(accounts[i]);
			System.out.println("============================");


		}
		/*
		Account a1= new  Savings(1000, "Saurabh", 10000);
		System.out.println(a1);
		a1.withdraw(5000);	  
		a1.callBalance();
		((KYC)a1).linkAdhar("1234 5678 0987 6433");
		System.out.println("=====================================");
		Account a2=new Current(1001, "Prashant", 20000, 10000);
		System.out.println(a2);
		a2.withdraw(5000);
		a2.callBalance();
		((KYC)a2).linkAdhar("1232 5178 0787 6233");
		System.out.println("=====================================");
		Account a3 = new Reccuring(1002, "Vishal", 100000, 1000, 5);
		System.out.println(a3);
		a3.withdraw(2000);
		a3.callBalance();
		*/

		
		for(Account a : accounts)
		{
			if(a instanceof KYC)
			{
				if(a instanceof Savings && ((Savings)a).getAdharno()!=null)
				{
					System.out.println("Acc No : "+a.getAc_no()+" Adhar no : "+((Savings)a).getAdharno());
				}
				
				if(a instanceof Current && ((Current)a).getAdharno()!=null)
				{
					System.out.println("Acc No : "+a.getAc_no()+" Adhar no : "+((Current)a).getAdharno());
				}
			}
		}

	}

}



