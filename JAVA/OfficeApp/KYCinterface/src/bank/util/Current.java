package bank.util;

public class Current extends Account implements KYC
{
 
	private String adharno;
	private double overdraft_amt;
	public Current() {
		// TODO Auto-generated constructor stub
	}

	
	

	public String getAdharno() {
		return adharno;
	}




	public void setAdharno(String adharno) {
		this.adharno = adharno;
	
        	
	
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
		return super.toString()+"\nOverdraft Amount : "+overdraft_amt+"\nAdhar No  : "+adharno;
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
	
	@Override
	public void linkAdhar(String adharno) 
	{
		int count=0;
		if(adharno.length()==19)
		{
			if(adharno.charAt(4)==' ' && adharno.charAt(9)==' ' && adharno.charAt(14)==' ')
			{
				for(int i=0;i<19;i++)
				{
					if(i!=4 && i!=9 && i!=14)
					{
						if(adharno.charAt(i)>=48 && adharno.charAt(i)<=56)
						{
							count++;
						}
					}
				}
			}
		}
		if(count==15)
		{
			this.adharno=adharno;
		}
		else
		{
			System.out.println("Enter the no in correct format ");
		}
	}

}
