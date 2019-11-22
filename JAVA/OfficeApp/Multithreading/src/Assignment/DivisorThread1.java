package Assignment;

import java.io.FileWriter;
import java.io.IOException;

public class DivisorThread1 implements Runnable {

	private int num;
	private Thread t;
	private FileWriter fw;
	


	public DivisorThread1(int num,FileWriter fw) {
		
		this.num = num;
		this.fw=fw;
		this.t = new Thread(this);
	}
	
	



	public int getNum() {
		return num;
	}





	public void setNum(int num) {
		this.num = num;
	}





	public Thread getT() {
		return t;
	}





	public void setT(Thread t) {
		this.t = t;
	}





	public void run() 
	{
		synchronized (fw) {
		for(int i=1;i<=num;i++)
		{
			if(num%i==0)
			{
				try {
					fw.write("Divisor of "+num+" : "+i);
					fw.write("\n");
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			
			
		}
		}
		
	}

}
