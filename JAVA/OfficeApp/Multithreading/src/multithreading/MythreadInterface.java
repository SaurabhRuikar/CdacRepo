package multithreading;

public class MythreadInterface implements Runnable {

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
		// TODO Auto-generated method stub

	}

}
