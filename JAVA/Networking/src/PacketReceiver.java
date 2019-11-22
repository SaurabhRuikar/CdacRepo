import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.SocketException;

public class PacketReceiver {

	public static void main(String[] args) {
		try
		{
			
			
			byte[] arr = new byte[1024];
			
			DatagramPacket packet = new DatagramPacket(arr, arr.length);
			
			DatagramSocket socket = new DatagramSocket(4500);
			
			socket.receive(packet);
			
			System.out.println("Length : "+packet.getLength());
			System.out.println("Port No  :"+packet.getPort());
			System.out.println("Address : "+packet.getAddress());
		
			String s = new String(packet.getData(),0,packet.getLength());
			System.out.println("Data:"+s);
					
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
