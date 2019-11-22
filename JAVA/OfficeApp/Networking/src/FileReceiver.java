import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class FileReceiver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		BufferedWriter bw=null;
		try
		{
		   bw=new BufferedWriter(new FileWriter("/home/student/Desktop/hello111.txt"));
			
			byte[] arr = new byte[1024];
			
			DatagramPacket packet = new DatagramPacket(arr, arr.length);
			
			DatagramSocket socket = new DatagramSocket(5999);
			
			socket.receive(packet);
			
			System.out.println("Length : "+packet.getLength());
			System.out.println("Port No  :"+packet.getPort());
			System.out.println("Address : "+packet.getAddress());
		
			String s = new String(packet.getData(),0,packet.getLength());
			System.out.println("Data:"+s);
			
			
			
				bw.write(s);
			
			bw.flush();
			bw.close();
					
		}
		catch(SocketException e)
		{
			e.printStackTrace();
		}
		catch(IOException e)
		{
			e.printStackTrace();
		}

	}

	}


