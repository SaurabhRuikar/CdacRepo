package office.staff;

public class Programmer extends employee 
{
	
	private double extraHour,chargesPerHour;

	public Programmer()
	{
		super();
		// TODO Auto-generated constructor stub
	}

	public Programmer(String name, int dd, int mm, int yy, int empid, double salary, double extraHour,
			double chargesPerHour)
	{
		super(name, dd, mm, yy, empid, salary);
		this.extraHour = extraHour;
		this.chargesPerHour = chargesPerHour;
	}

	@Override
	public void display() 
	{
		super.display();
		System.out.println("Extra Hours   : "+extraHour);
		System.out.println("Charges Per Hour : "+chargesPerHour);
	}

	
	@Override
	public double calSalary() 
	{
		// TODO Auto-generated method stub
		return salary+extraHour*chargesPerHour;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nExtraHours : "+extraHour+"\nChargesPerHours : "+chargesPerHour;
	}
	

}
