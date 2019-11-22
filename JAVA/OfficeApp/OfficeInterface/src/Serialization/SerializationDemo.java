package Serialization;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

import office.staff.Admin;
import office.staff.Programmer;
import office.staff.SalesManager;
import office.staff.employee;

public class SerializationDemo {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		// TODO Auto-generated method stub
		employee [] e =new employee[3];
		e[0]=new SalesManager("Prashant", 18, 5, 1997, 1, 100000, 150000, 4.5,8);
		e[1]=new Programmer("Saurabh", 12, 12, 1998, 2, 200000, 42.2, 545,8);
		e[2]=new Admin("Vishal", 13, 3, 1997, 3, 19899, 1000);
		
		ObjectOutputStream oos=new ObjectOutputStream(new FileOutputStream("/home/student/Desktop/empnew.txt"));
		for(employee s:e)
		{
			oos.writeObject(s);
			
		}
		
		oos.close();
		
		
		
	}

}
