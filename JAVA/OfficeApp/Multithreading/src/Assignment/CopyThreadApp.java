package Assignment;

import java.util.Scanner;

public class CopyThreadApp 
{

	public static void main(String[] args) throws InterruptedException 
	{
		Scanner sc =new Scanner(System.in);
		String destination,source,ans;
		CopyThread c = null;
		System.out.println("Enter source path");
		source = sc.next();
		System.out.println("Enter destination path");
		destination = sc.next();
		System.out.println("Do you want to append or not");
		ans = sc.next();
		
		if(ans.equals("y"))
			c = new CopyThread(source, destination, true);
		else
			c = new CopyThread(source, destination, false);
		
		c.getT().start();
		
		c.getT().join();
		System.out.println("File is copied");
		
}

}
