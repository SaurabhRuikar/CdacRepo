package Assignment;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class DisplayFile implements Runnable{

	
	
	private Thread t;
	private BufferedReader br;
	
	
	public DisplayFile() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	public DisplayFile(BufferedReader br) {
		super();
		this.br=br;
		this.t = new Thread(this);
	}
	



	public Thread getT() {
		return t;
	}

	public void setT(Thread t) {
		this.t = t;
	}
	


	@Override
	public void run() {
		synchronized (System.out) {
			
					try {
						String i;
						while((i=br.readLine())!=null)
						{
							System.out.println(i);
								
							
						}
						
					} catch (IOException e) {
						// TODO Auto-generated catch block
						e.printStackTrace();
					}
		
				
		}
		
	}
	

}