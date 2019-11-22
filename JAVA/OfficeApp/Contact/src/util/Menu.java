package util;

import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import app.NumberException;
import app.errorException;
import app.mailException;

public class Menu
{

	public void menu() throws IOException, Exception 
	{
		
	
		
		 Scanner sc=new Scanner(System.in);
		 String y;
		 List<Contact> c = new ArrayList<Contact>();
		 ObjectOutputStream o = new ObjectOutputStream(new FileOutputStream("/home/student/Desktop/contact.txt"));
		 do
		 {
			 System.out.println("======MENU======");
			 System.out.println("1.add\n2.delete\n3.update\n4.Show\n5.exit");
			 System.out.println("Enter your choice");
			 int ch=sc.nextInt();
			 
			 switch(ch)
			 {
			 	case 1: System.out.println("Enter the Name :");
			 			String name = sc.next();
			 			

		     System.out.println("Enter Email : ");
			 			String mail = sc.next();
			 			if(mail.contains("@"))
			 			{
			 				System.out.println(" ");
			 			}
			 			else
			 			{  
			 				
			 				throw new mailException();
			 			}
			 			System.out.println("Enter the Mob : ");
			 		 	
			 			String mob = sc.next();
			 			if(mob.length()==10)
			 			{
			 				System.out.println("");
			 			}
			 			else
			 			{
			 				throw new NumberException();
			 			}
			 			
			 			c.add(new Contact(name, mail, mob));
			 			break;
			 		
			 	case 2: System.out.println("Name to delete : ");
			 			String dname = sc.next();
			 			int l=1000;
			 			for(Contact c2 : c)
			 			 {
			 			
			 				if((c2.getName()).equals(dname))
			 				{
			 					l = c.indexOf(c2);
			 					System.out.println(l);
			 					
			 				}
			 			 }
			 			 c.remove(l);
			 			 break;
			 	case 3: System.out.println("Name to update : ");
			 			String uname = sc.next();
			 			System.out.println("Enter new Name :");
			 			String name1 = sc.next();
			 			System.out.println("Enter new Email : ");
			 			String mail1 = sc.next();
			 			System.out.println("Enter new the Mob : ");
			 			String mob1 = sc.next();
			 			int g;
			 			for(Contact c2 : c)
			 			 {
			 			
			 				if((c2.getName()).equals(uname))
			 				{	
			 					g = c.indexOf(c2);
			 					c.set(g, new Contact(name1, mail1, mob1));
					 	    }
		
			 			 }			                  
                         break;

			 	case 4: for(Contact c1 : c)
			 			{
			 				System.out.println(c1);
			 			}
			 			break;
			 	case 5: for(Contact c1 : c)
				 		{
					 		o.writeObject(c1);
				 		}
			 			System.out.println("Exiting");
			 			System.exit(0);
			 }

			 System.out.println("Do you want to continue : ");
			 y = sc.next();
		 }while(y.equals("y") || y.equals("Y"));
		 
		 for(Contact c1 : c)
	 	{
	 		o.writeObject(c1);
		}
		 
	}

}
