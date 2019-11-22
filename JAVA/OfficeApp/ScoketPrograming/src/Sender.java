import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class Sender {

	public static void main(String[] args) throws Exception{
	
		
		
		
		String s ="TEST_DATA";
		byte[] arr=s.getBytes();
		InetAddress address=InetAddress.getByName("localhost");
		DatagramPacket packet = new DatagramPacket(arr, arr.length,address,4000);
		DatagramSocket socket = new DatagramSocket(5000);
		socket.send(packet);
	}

}
