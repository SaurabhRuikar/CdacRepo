package udp;


import java.io.BufferedReader;

import java.io.InputStreamReader;

import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

import java.util.Calendar;

public class ServerMain 
{

	public static void main(String[] args) throws Exception
	{
		
		ServerSocket ss = new ServerSocket(5000);
		System.out.println("server is ready");
		
		while(true)
		{
			
			Socket clsoc=ss.accept();
			System.out.println("client_connected");
			BufferedReader br=new BufferedReader(new InputStreamReader(clsoc.getInputStream()));
			PrintWriter out =new PrintWriter(new OutputStreamWriter(clsoc.getOutputStream()));
			
		
			String ctime =Calendar.getInstance().getTime().toString();
			out.print(ctime+"\n");
			out.flush();
			while(true)
			{
				String ack=br.readLine();
				if(ack!=null)
				{
					System.out.println("Acknowledge : "+ack);
					break;
				}
				
			}
		}

	}

}
