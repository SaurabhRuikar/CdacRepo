package file;

import java.io.BufferedReader;
import java.io.FileReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class FileSender {

	public static void main(String[] args) throws Exception
	{
		DatagramSocket socket = null;
		
		BufferedReader br = new BufferedReader(new FileReader("/home/student/Desktop/hello.txt"));
		String s;
		while((s=br.readLine())!=null)
		{
			s=s.concat(s);
		}
		
		byte[] arr=s.getBytes();
		InetAddress address=InetAddress.getByName("localhost");
		DatagramPacket packet = new DatagramPacket(arr, arr.length,address,40012);
		socket = new DatagramSocket(5010);
		socket.send(packet);
		
		br.close();
		socket.close();
		
	}

}
