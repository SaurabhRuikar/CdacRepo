package bank.util;

public class Current extends Account {
 
	
	private double overdraft_amt;
	public Current() {
		// TODO Auto-generated constructor stub
	}

	
	

	public Current(int ac_no, String name, double balance, double overdraft_amt) 
	{
		super(ac_no, name, balance);
		this.overdraft_amt = overdraft_amt;
	}




	@Override
	public void withdraw(double amt) 
	{
		if((balance+overdraft_amt)!=0)
		{
			System.out.println("You can withdraw upto  :"+(balance+overdraft_amt));		
		}
		else
		{
			
			System.out.println("\nYoure account balance is low");
			
		}
		System.out.println("remaining balance is :"+balance);
	}




	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nOverdraft Amount : "+overdraft_amt;
	}




	@Override
	public void callBalance() {
		if(overdraft_amt<100000)
			System.out.println("balance"+(balance-5000));
		else if(overdraft_amt >= 100000 && overdraft_amt <= 500000)
			System.out.println("balance "+ (balance-7000));
		else if(overdraft_amt >= 500000 && overdraft_amt <= 1000000)
			System.out.println("balance "+ (balance-10000));
		
	}




	
	
	
	

}
