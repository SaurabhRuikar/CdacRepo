package threadapps;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadThread implements Runnable {
	private Thread t;
	private BufferedReader br;
	 public ReadThread(BufferedReader br) {
		// TODO Auto-generated constructor stub
		t=new Thread(this);
		this.br=br;
	}
	 
	public Thread getT() {
		return t;
	}





	public void setT(Thread t) {
		this.t = t;
	}






	public BufferedReader getBr() {
		return br;
	}






	public void setFr(BufferedReader br) {
		this.br = br;
	}













	@Override
	public void run() {
		// TODO Auto-generated method stub
		//synchronized (System.out) 
		//{
		try
		{
			String str;
			while((str=br.readLine())!=null)
			{
				System.out.println(str);
				Thread.sleep(100);
			}
			
		}
			catch (Exception e)
			{
				e.printStackTrace();
			}
			
			
			
			
		//}
	}


	
	
	


}
