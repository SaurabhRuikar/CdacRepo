package bank.util;

 public class Savings extends Account implements KYC
{
	private static double int_rate;
	private String adharno;
	
	static
	{
		int_rate=8.8;	
	}
	
	
	
	public String getAdharno() {
		return adharno;
	}


	public void setAdharno(String adharno) {
		this.adharno = adharno;
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
		return super.toString()+"\nIntrest rate : "+int_rate+"\nAdhar no  : "+adharno;
	}


	@Override
	public void callBalance() {
		System.out.println("balance is :"+(balance+(balance*int_rate)/100 ));
		
		
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
