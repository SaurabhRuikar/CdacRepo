package app;

import office.staff.Admin;
import office.staff.ITraveller;
import office.staff.Programmer;
import office.staff.SalesManager;
import office.staff.employee;


public class EmployeeDemo 
{
	public static void main(String[] args) 
	{
		employee [] e =new employee[3];
		e[0]=new SalesManager("Prashant", 18, 5, 1997, 1, 100000, 150000, 4.5,8);
		e[1]=new Programmer("Saurabh", 12, 12, 1998, 2, 200000, 42.2, 545,8);
		e[2]=new Admin("Vishal", 13, 3, 1997, 3, 19899, 1000);
		double total = 0;
		for(int i=0;i<e.length;i++)
		{
			//*e[i].display();
			total = total + e[i].calSalary();
			System.out.println(e[i]);
			System.out.println("Net Salary : "+e[i].calSalary());
			
			if(e[i] instanceof ITraveller)
			{
				System.out.println("Travelling Allowance : "+((ITraveller)e[i]).calculateTa());
			}
			
			System.out.println("===============================");	
		}	
		System.out.println(" Total salary is :"+total+"    |");
		System.out.println("===============================");
		
		for(employee q : e )
		{
			if(q instanceof SalesManager && q instanceof ITraveller)
				System.out.println(q.getEmpid()+" : "+((SalesManager)q).getDays()+" : "+((ITraveller)q).calculateTa());
			else if(q instanceof Programmer && q instanceof ITraveller)
				System.out.print(q.getEmpid()+" : "+((Programmer)q).getDays()+" : "+((ITraveller)q).calculateTa());
		}
	}
}


