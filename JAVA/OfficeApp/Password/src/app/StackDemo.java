package app;
import java.io.Console;

import stack.util.Stack;
import stack.util.StackOverflow;
import stack.util.StackUnderflow;


public class StackDemo {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		try
		{
			Stack s = new Stack();
			//Console c = System.console();
			//System.out.println("enter number");
	        //int t = Integer.parseInt(c.readLine());
			s.push(10);	
			s.push(20);	
			s.push(30);	
			
			s.pop();	
			
			s.pop();
			s.pop();
			s.pop();
			s.pop();
			s.display();
		}
		catch(StackOverflow | StackUnderflow e)
		{
			System.out.println(e);
		}
	}

}
