package app;

import office.staff.Admin;
import office.staff.Programmer;
import office.staff.SalesManager;
import office.staff.employee;
import java.util.*;



public class EmployeeUser
{
	public static void main(String[] args) 
	{   
		Scanner s=new Scanner(System.in);
		System.out.println("enter ename");
		String name=s.next();
		System.out.println("enter bithdate");
		int dd=s.nextInt();
		int mm=s.nextInt();
		int yy=s.nextInt();
		System.out.println("enter empid");
		int empid=s.nextInt();
		System.out.println("enter salary");
		double salary=s.nextDouble();
		System.out.println("enter target");
		double target=s.nextDouble();
		System.out.println("enter incentive");
		double incentive=s.nextDouble();


		employee [] e =new employee[3];
		e[0]=new SalesManager(name,dd,mm,yy,empid,salary,target,incentive,8);

		e[1]=new Programmer("saurabh", 12, 12, 1998, 2, 20000, 42.2, 545,8);
		e[2]=new Admin("vishal", 13, 3, 1997, 2, 19899, 1000);

		for(int i=0;i<e.length;i++)
		{
			e[i].display();
			System.out.println("============================");	
		}	
	}
}



