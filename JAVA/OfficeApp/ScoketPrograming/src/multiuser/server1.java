package multiuser;
import java.net.*;
import java.util.Scanner;
import java.io.*;

class user implements Runnable
{
	Socket cli_soc;
	String str,str1;

	Scanner s= new Scanner(System.in);
	user(Socket soc)
	{
		this.cli_soc = soc;
	}
	
	public void run() 
	{
		
		
		try{
		
			DataInputStream in = new DataInputStream(cli_soc.getInputStream());
			DataOutputStream out = new DataOutputStream(cli_soc.getOutputStream());
			
			while(true)
			{ System.out.println("Receiver : ");
				str = in.readUTF();
				System.out.println("client says :"+Thread.currentThread().getName()+" :" + str);
			
				str1= s.nextLine();
				out.writeUTF(str1);
				
				out.flush();
				
				
			}
		}catch(Exception e)
		{
			System.out.println(e);
		}
	}
}

class server1
{
	public static void main(String args[]) throws IOException
	{
		ServerSocket ser = new ServerSocket(6602);
		Socket soc1;
		
	
		
		while(true)
		{
			soc1 = ser.accept();
			new Thread(new user (soc1)).start();
		}
		
	}
}