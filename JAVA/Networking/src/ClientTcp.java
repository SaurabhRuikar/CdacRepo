import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketException;

public class ClientTcp {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Socket s = null;
		BufferedReader br = null;
		PrintWriter out = null;
		
		try
		{
			
		
		s = new Socket("127.0.0.1",5300);
		
		br = new BufferedReader(new InputStreamReader(s.getInputStream()));
		out = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
		
		while(true)
		{
			String str = br.readLine();
			if(str != null)
			{
				System.out.println("Current time is : "+str);
			}
			String ack = "Thanks received time \n";
			out.print(ack);
			out.flush();
			break;
		
		
		
		}
		
		}
		catch(SocketException e)
		{
			e.printStackTrace();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}
		finally
		{
			try {
				br.close();
				out.close();
				s.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
	}

}
