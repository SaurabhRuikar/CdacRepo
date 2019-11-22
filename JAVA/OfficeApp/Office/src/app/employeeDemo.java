package app;

import office.staff.Admin;
import office.staff.Programmer;
import office.staff.SalesManager;
import office.staff.employee;


public class employeeDemo 
{
	public static void main(String[] args) 
	{
		employee [] e =new employee[3];
		e[0]=new SalesManager("Prashant", 18, 5, 1997, 1, 100000, 150000, 4.5);
		e[1]=new Programmer("Saurabh", 12, 12, 1998, 2, 200000, 42.2, 545);
		e[2]=new Admin("Vishal", 13, 3, 1997, 2, 19899, 1000);
		double total = 0;
		for(int i=0;i<e.length;i++)
		{
			//*e[i].display();
			total = total + e[i].calSalary();
			System.out.println(e[i]);
			System.out.println("Net Salary : "+e[i].calSalary());
			System.out.println("============================");	
		}	
		System.out.println(" Total salary is :"+total+" |");
		System.out.println("============================");
		
	}
}


