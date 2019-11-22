                            package app;

import office.util.Person;

public class PersonDemo 
{
	public static void main(String[] args) 
	{
		Person p1 = new Person("Monty", 12, 10, 1928);
		p1.display();
		Person p2 = new Person();
		p2.display();
	}
}
