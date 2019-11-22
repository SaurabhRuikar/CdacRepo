package office.staff;

public class Programmer extends employee implements ITraveller
{
	
	private double extraHour,chargesPerHour;
	private int days;
	
	

	public int getDays() {
		return days;
	}



	public void setDays(int days) {
		this.days = days;
	}



	public Programmer()
	{
		super();
		// TODO Auto-generated constructor stub
	}

	

	public Programmer(String name, int dd, int mm, int yy, int empid, double salary, double extraHour,
			double chargesPerHour, int days) {
		super(name, dd, mm, yy, empid, salary);
		this.extraHour = extraHour;
		this.chargesPerHour = chargesPerHour;
		this.days = days;
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
		return salary+extraHour*chargesPerHour+calculateTa();
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nExtraHours : "+extraHour+"\nChargesPerHours : "+chargesPerHour+"\nDays Travelled :"+days;
	}

	@Override
	public double calculateTa() {
		// TODO Auto-generated method stub
		return (salary*Da/100)*days;
	}
	

}
