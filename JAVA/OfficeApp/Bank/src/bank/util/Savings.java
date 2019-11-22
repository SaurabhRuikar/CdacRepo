package bank.util;

 public class Savings extends Account 
{
	private static double int_rate;
	
	static
	{
		int_rate=8.8;	
	}
	
	public Savings() 
	{
		// TODO Auto-generated constructor stub
	}


	public Savings(int ac_no, String name, double balance) 
	{
		super(ac_no, name, balance);
		
	}

	@Override
	public void withdraw(double amt) 
	{
		if(balance-amt>=1000)
		{
			System.out.println("Your balnce is   :"+balance+"\nYou can withdraw upto   "+(balance-1000));
			
		}
		else 
		{
			System.out.println("Your Account balnce is low");
			
		}
		
		
	}


	@Override
	public String toString() 
	{
		// TODO Auto-generated method stub
		return super.toString()+"\nIntrest rate : "+int_rate;
	}


	@Override
	public void callBalance() {
		System.out.println("balance is :"+(balance+(balance*int_rate)/100 ));
		
		
	}
	
	

}
