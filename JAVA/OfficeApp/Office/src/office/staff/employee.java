package office.staff;

import office.util.Person;

public abstract class employee extends Person{

	
	private int empid;
	protected double salary;
	
	public employee() 
	{
		super();
		empid=0;
		salary=0;
    }



	public employee(String name, int dd, int mm, int yy,int empid, double salary) 
	{
		super(name, dd, mm, yy);
		this.empid=empid;
		this.salary=salary;		
	}



	public void display()
	{
        super.display();
		System.out.println("empid : "+empid);
		System.out.println("salary : "+salary);
		
	}

	public abstract double calSalary();


	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString()+"\nEmpid      : "+empid+"\nSalary     : "+salary;
	}
	
	
}
