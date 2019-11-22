package app;

import bank.util.Account;
import bank.util.Current;
import bank.util.Reccuring;
import bank.util.Savings;

public class BankDemo {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		/*	Account [] accounts = {
				                new Savings(1000, "Saurabh", 10000),
								new Current(1001, "Prashant", 20000, 10000),
								new Reccuring(1002, "vishal", 100000, 1000, 5)
		                      };



		for(int i=0;i<accounts.length;i++)
		{

			System.out.println(accounts[i]);
			System.out.println("============================");


		}*/
		Account a1= new  Savings(1000, "Saurabh", 10000);
		System.out.println(a1);
		a1.withdraw(5000);	  
		a1.callBalance();
		System.out.println("=====================================");
		Account a2=new Current(1001, "Prashant", 20000, 10000);
		System.out.println(a2);
		a2.withdraw(5000);
		a2.callBalance();
		System.out.println("=====================================");
		Account a3 = new Reccuring(1002, "Vishal", 100000, 1000, 5);
		System.out.println(a3);
		a3.withdraw(2000);
		a3.callBalance();


	}

}



