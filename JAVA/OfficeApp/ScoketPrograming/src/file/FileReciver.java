package file;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class FileReciver {

	public static void main(String[] args) throws Exception
	{
		DatagramSocket socket = null;
		BufferedWriter bw = null;
		byte []arr=new byte [1024];
		
		DatagramPacket packet= new DatagramPacket(arr, arr.length);
		socket= new DatagramSocket(40012);
		socket.receive(packet);
		String s =new  String(packet.getData(),0,packet.getLength());
		System.out.println("reciving");
		bw =  new BufferedWriter(new FileWriter("/home/student/Desktop/hello11.txt"));
		bw.write(s);
		socket.close();
		bw.close();

	}

}
