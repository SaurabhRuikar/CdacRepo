package bank.util;

public class Reccuring extends Account {
	
	
	private  double recurring_amt;
	private int no_installment;
	private double up_balance=0;
    private static double int_rate1;
	
	static
	{
		int_rate1=7.5f;	
	}
	

	public Reccuring() {
		// TODO Auto-generated constructor stub
	}



	public Reccuring(int ac_no, String name, double balance, double recurring_amt, int no_installment) 
	{
		super(ac_no, name, balance);
		this.recurring_amt = recurring_amt;
		this.no_installment = no_installment;
	}



	@Override
	public void withdraw(double amt) 
	{
		System.err.println("Cant withdraw from this account");
		  
	}



	@Override
	public String toString() 
	{
		// TODO Auto-generated method stub
         up_balance=balance+recurring_amt*no_installment;
		return super.toString()+"\nRecurring Amount : "+recurring_amt+"\nNo of Installments : "+no_installment+"\nupdated balance :"+up_balance;
	}



	@Override
	public void callBalance() {
		System.out.println("balance is :"+(+balance+recurring_amt*no_installment+(recurring_amt*no_installment*int_rate1)/100 ));
		
		
	}
	
	
	

}
