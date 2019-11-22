package udp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

public class client {

	public static void main(String[] args) throws UnknownHostException, IOException {
		// TODO Auto-generated method stub

	
	Socket s =new Socket("127.0.0.1", 5000);
	BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
	PrintWriter out = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
	while(true)
	{
		
		String str =br.readLine();
		if(str != null)
		{
			System.out.println("Curent time : "+str);
			String ack = "thanks";
			out.print(ack);
			out.flush();
			break;
		}
		
	}
	
	
	}

}
