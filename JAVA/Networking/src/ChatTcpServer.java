import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;
import java.util.Calendar;

public class ChatTcpServer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		
		    
		
			ServerSocket sc = null;
			try
			{
				
			PrintWriter out = null;
			BufferedReader br = null;
			BufferedReader br1=null;
			Socket clsoc = null;
			
			sc = new ServerSocket(5300);
			System.out.println("Server Ready");
			
			while(true)
			{
				clsoc = sc.accept();
				System.out.println("Client Connected");
				
				br = new BufferedReader(new InputStreamReader(clsoc.getInputStream()));
				out = new PrintWriter(new OutputStreamWriter(clsoc.getOutputStream()));
				br1= new BufferedReader(new InputStreamReader(System.in));
				String ctime = Calendar.getInstance().getTime().toString();
				
				out.print("Time:"+ctime+"\n");
				out.flush();
				while(true)
				{
					String ack = br.readLine();
					if(ack != null)
					{
						System.out.println("Message from client : "+ack);
						if(ack.equals("bye"))
						{
							break;
						}
						System.out.println("Enter message : ");
						String msg = br1.readLine();
						
						out.print(msg+"\n");
						out.flush();
					}
					
				}
				
				
				br.close();
				out.close();
				clsoc.close();
			
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
				try
				{
					sc.close();
				} catch (IOException e) 
				{
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
	}
	}


