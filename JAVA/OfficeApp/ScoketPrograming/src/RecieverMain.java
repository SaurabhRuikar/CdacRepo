import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class RecieverMain {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		byte []arr=new byte [1024];
		DatagramPacket packet= new DatagramPacket(arr, arr.length);
		DatagramSocket socket= new DatagramSocket(4000);
		socket.receive(packet);
		System.out.println("length :  "+ packet.getLength());
		System.out.println("port no : "+packet.getPort());
		String s =new  String(packet.getData(),0,packet.getLength());
		System.out.println("Data :"+s);

	}

}
