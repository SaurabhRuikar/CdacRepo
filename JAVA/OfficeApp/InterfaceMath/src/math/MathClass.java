package math;

public class MathClass implements MathOperations {
	
	
	

	public MathClass() {
		super();
		// TODO Auto-generated constructor stub
	}

	@Override
	public boolean isPrime(int n)
	{
		int count = 0;
		for(int i=1;i<=(n/2);i++)
		{
			if(n%i==0)
			{
				count++;
			}	
		}
		
		if(count<2)
			return true;
		else 
			return false;
	}

	@Override
	public boolean isPallindrom(int n) 
	{
		int temp=n,rev=0;
		while(n>0)
		{
			rev = rev*10+n%10;
			n=n/10;
		}
		
		if(temp==rev)
			return true;
		else
			return false;
	}

	@Override
	public double getFactorial(int n) 
	{
		double fact = 1;
		for(int i=1;i<=n;i++)
		{
			fact = fact*i;
		}
		return fact;
	}

}
