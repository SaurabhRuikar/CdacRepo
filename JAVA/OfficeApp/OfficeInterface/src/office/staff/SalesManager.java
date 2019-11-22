package office.staff;

public class SalesManager extends employee implements ITraveller
{

	private double target,incentive;
	private int days;
	
	
	
	public int getDays() {
		return days;
	}

	public void setDays(int days) {
		this.days = days;
	}

	public SalesManager() 
	{
		
	}

	public SalesManager(String name, int dd, int mm, int yy, int empid, double salary, double target, double incentive,
			int days) {
		super(name, dd, mm, yy, empid, salary);
		this.target = target;
		this.incentive = incentive;
		this.days = days;
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
		return salary+target*incentive/100+calculateTa();
	}



	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nTarget     : "+target+"\nIncetive   : "+incentive+"\nDays Travelled :"+days;
	}



	@Override
	public double calculateTa() {
		// TODO Auto-generated method stub
		return (salary*Da/100)*days;
	}
	
	
	
}
