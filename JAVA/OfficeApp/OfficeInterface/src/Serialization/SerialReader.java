package Serialization;

import java.awt.List;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;

import office.staff.employee;

public class SerialReader {

	public static void main(String[] args) throws ClassNotFoundException, IOException
	{
	
		employee[] em=new employee[3];
		
		ObjectInputStream ois=new ObjectInputStream(new FileInputStream("/home/student/Desktop/empnew.txt"));
		String str;
		
		for(int i=0 ; i<3;i++)
		{
			
			em[i]=(employee)ois.readObject();
			
		}
		for(employee e:em)
		{
			System.out.println(e);
			System.out.println("===========================");
			
		}

	}

}
