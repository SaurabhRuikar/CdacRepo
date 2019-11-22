package BookDemo;

import java.util.Scanner;

import book.Book_id;
import book.Ebook;
import book.IdNotfoundException;
import book.Paper_book;

public class BookDemo 
{


	public static void main(String[] args) 
	{
	
		Book_id [] b = {new Paper_book("Java", 1500),new Paper_book("Oracle", 1200),new Paper_book("Python", 2000),
						new Ebook("C++", 1000),new Ebook("c", 150)};
		
		for(Book_id e : b )
		{
			System.out.println(e);
		}
		
		Scanner s = new Scanner(System.in);
		System.out.println("Enter the Id : ");
		int i = s.nextInt();
		System.out.println("Enter type of book : ");
		String str = s.nextLine();
		try
		{
			
			for(Book_id e : b )
		{
				
				if(e instanceof Paper_book && i == e.getId() && str.equals(e.getName()))
					System.out.println(e.calCost());
				else if(e instanceof Paper_book && i == e.getId() && str.equals(e.getName()))
					System.out.println(e.calCost());
				else
					throw new IdNotfoundException();
		
		}
		}
		catch(IdNotfoundException e)
		
		{
			e.getMessage();
		}
	}
}


