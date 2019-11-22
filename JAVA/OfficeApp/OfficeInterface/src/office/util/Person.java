package office.util;

import java.io.Serializable;

public class Person implements Serializable 
{
	private String name;
	private Date bdate;
	public Person() 
	{
		
	}
	public Person(String name, int dd, int mm, int yy) 
	{
		this.name = name;
		this.bdate = new Date(dd, mm, yy);
	}
	
	public void display()
	{
		System.out.println("Name : "+name);
		
		if(bdate!=null)
		{
			System.out.print("Bdate : ");
			bdate.showDate();
		}
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Name       : "+name+"\nBdate      : "+bdate;
	}
	
	
}
