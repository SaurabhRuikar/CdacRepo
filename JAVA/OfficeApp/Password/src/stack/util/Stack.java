package stack.util;
import java.io.Console;

public class Stack
{
	int[] stack;
	int top;
	int size;

	public Stack() throws StackOverflow, StackUnderflow
	{
		top = -1;
		size = 5;
		stack=new int[size];
	}
	
		public void push(int s) throws StackOverflow
		{
			
			if(top==size)
			{
				throw new StackOverflow();
			}  
			else
			{
				top++;
				stack[top]=s;
			}	
		}
		public void pop() throws StackUnderflow
		{
			if(top==-1)
			{
				throw new StackUnderflow();
			}  
			else
			{
				top--;
				
			}	
		}

		public void display()
		{
			if(top==-1)
			{
				System.out.println("stack is empty");
			}  
			else
			{
				for(int i=0;i<top;i++)
				{
					System.out.println(stack[i]);
				}	
			}	
		}

}
