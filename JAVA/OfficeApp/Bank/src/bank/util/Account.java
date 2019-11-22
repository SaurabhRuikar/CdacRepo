package bank.util;

public abstract class Account 
{
	protected int ac_no;
	protected String name;
	protected double balance;
	
	public Account() 
	{
		super();
		// TODO Auto-generated constructor stub
	}

	public Account(int ac_no, String name, double balance) 
	{
		super();
		this.ac_no = ac_no;
		this.name = name;
		this.balance = balance;
	}
	
	public abstract void withdraw(double amt);

	@Override
	public String toString() 
	{
		return "Account no : "+ac_no+"\nName : "+name+"\nBalance  : "+balance;
	}
	public abstract void callBalance();	
}
