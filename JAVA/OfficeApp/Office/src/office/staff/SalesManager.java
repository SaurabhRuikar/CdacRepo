package office.staff;

public class SalesManager extends employee 
{

	private double target,incentive;
	
	public SalesManager() 
	{
		
	}

	

	public SalesManager(String name, int dd, int mm, int yy, int empid, double salary, double target,
			double incentive) 
	{
		super(name, dd, mm, yy, empid, salary);
		this.target = target;
		this.incentive = incentive;
	}



	@Override
	public void display() 
	{
		super.display();
		System.out.println("Target     :"+target);
		System.out.println("Incentive  :"+incentive);
	}

	

	@Override
	public double calSalary() 
	{
		// TODO Auto-generated method stub
		return salary+target*incentive/100;
	}



	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nTarget     : "+target+"\nIncetive   : "+incentive;
	}
	
}
