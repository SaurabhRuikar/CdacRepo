package app;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import javax.crypto.CipherInputStream;

import util.Contact;
import util.Menu;

public class ContactDemo 
{

	public static void main(String[] args) throws Exception 
	{
		Menu m = new Menu();
		m.menu();
		List<Contact> c = new ArrayList<Contact>();
		ObjectInputStream o = new ObjectInputStream(new FileInputStream("/home/student/Desktop/contact.txt"));
		while(true)
		{
			try
			{
				c.add((Contact)o.readObject());
			}
			catch(Exception e)
			{
				break;
			}
		}
		
		for(Contact c1 : c)
		{
			System.out.println(c1);
			System.out.println("===================");
		}
	}

}
