package Assignment;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class CopyThread implements Runnable 
{

	private String destination,source;
	private boolean append;
	private Thread t;	
	
	public CopyThread(String source, String destination,boolean append) 
	{
		super();
		this.destination = destination;
		this.source = source;
		t = new Thread(this);
		this.append = append;
	}

	

	public String getDestination() {
		return destination;
	}



	public void setDestination(String destination) {
		this.destination = destination;
	}



	public String getSource() {
		return source;
	}



	public void setSource(String source) {
		this.source = source;
	}



	public Thread getT() {
		return t;
	}



	public void setT(Thread t) {
		this.t = t;
	}



	public void run() 
	{
		try
		{
			BufferedReader br = new BufferedReader(new FileReader(source));
			BufferedWriter bw = new BufferedWriter(new FileWriter(destination,append));
			String s;
			while((s=br.readLine())!=null)
			{
				bw.write(s);
				bw.newLine();
			}
			br.close();
			bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
		
	}

}
