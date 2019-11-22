import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class FileSender {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		BufferedReader br=null;
		try
		{
			DatagramSocket socket = new DatagramSocket(5000);
			br=new BufferedReader(new FileReader("/home/student/Desktop/1.txt"));
			 String ss,fina="";
			 while((ss=br.readLine())!=null)
			 {
			
				 fina = fina.concat("\n");
				 fina=fina.concat(ss);
				 
			 }
			 System.out.println(fina);
			byte[] arr = fina.getBytes();
			
			InetAddress address = InetAddress.getByName("localhost");
			
			DatagramPacket packet = new DatagramPacket(arr,arr.length,address,5999);
			
			
			socket.send(packet);
		
		
			 br.close();
			 socket.close();
			 
		}
		catch(UnknownHostException e)
		{
			System.out.println("Host not found");
		}
		catch(IOException e)
		{
			System.out.println("IO EXCEPTION ERROR");
		}
		
		}

		


	}


