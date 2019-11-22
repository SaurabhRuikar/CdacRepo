package multiuser;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

class client1
{
	public static void main(String args[]) throws IOException
	{
		Scanner s = new Scanner(System.in);
		Socket soc = new Socket("localhost",6602);
		String str,str1;
		try {
	
			DataInputStream in = new DataInputStream(soc.getInputStream());
			DataOutputStream out = new DataOutputStream(soc.getOutputStream());
	
			while(true)
			{
				System.out.println("Client :");
				str = s.nextLine();
				out.writeUTF(str);
		        
				str1 = in.readUTF();
				System.out.println("Reciever says : " + str1);
			
			
			
			}
		
		
		
		
		}catch(Exception e)
		{
			System.out.println(e);
		}
		soc.close();
	}
}