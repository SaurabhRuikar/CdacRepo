package multithreading;

public class ThreadCount implements Runnable 
{
	private Thread t;
	private int num;
	private String name;
	
	public ThreadCount(int cnt,String name) 
	{
		super();
		this.num = cnt;
		t = new Thread(this);
		this.name = name;
	}

	

	@Override
	public void run() 
	{
		while(num>0)
		{
			System.out.println(name+" thread prints : "+num--);
			try {
				Thread.sleep(10);
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




	public String getName() {
		return name;
	}



	public void setName(String name) {
		this.name = name;
	}
	
	

}
