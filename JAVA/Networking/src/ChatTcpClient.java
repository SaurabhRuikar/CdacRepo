import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.SocketException;

public class ChatTcpClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
			
			Socket s = null;
			BufferedReader br = null;
			PrintWriter out = null;
			BufferedReader br1=null;
			
			try
			{
				
			
			s = new Socket("127.0.0.1",5300);
			
			br = new BufferedReader(new InputStreamReader(s.getInputStream()));
			out = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
			br1= new BufferedReader(new InputStreamReader(System.in));
			String ack=null;
			while(true)
			{
				String str = br.readLine();
				if(str != null)
				{
					System.out.println("meesage from server : "+str);
					
					System.out.println("Enter the message");
					 
					 
					ack = br1.readLine();
					out.print(ack+"\n");
					out.flush();
					if(ack.equals("bye"))
					{
						break;
					}
					
					
				}
				
			
			
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
					br1.close();
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


