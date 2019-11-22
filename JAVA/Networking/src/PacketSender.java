import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class PacketSender {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		try
		{
			String s = "Test data for UDP communication";
			byte[] arr = s.getBytes();
			
			InetAddress address = InetAddress.getByName("localhost");
			
			DatagramPacket packet = new DatagramPacket(arr,arr.length,address,4500);
			
			DatagramSocket socket = new DatagramSocket(5500);
			
			socket.send(packet);
		
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
