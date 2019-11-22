package multithreading;

public class ThreadInInterface implements Runnable 
{
	private Thread t;
	
	
	public ThreadInInterface()
	{
		t = new Thread(this);
		
		// TODO Auto-generated constructor stub
	}


	@Override
	public void run() 
	{
		for(int i=0;i<5;i++)
		{
			System.out.println("Child thred : "+i);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}


	public Thread getT() {
		return t;
	}


	public void setT(Thread t) {
		this.t = t;
	}
	
	

}
