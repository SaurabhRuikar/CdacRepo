package app;

import multithreading.MytThreadClass;
import multithreading.MythreadInterface;
import multithreading.ThreadInInterface;

public class ThreadApp {

	public static void main(String[] args) throws InterruptedException {
		 //Thread t=new MytThreadClass();
		 //t.start();
		
		
		 //Runnable r = new MythreadInterface();
		 //Thread t1 = new Thread(r);
		 //t1.start();
		
		ThreadInInterface e1 = new ThreadInInterface();
		e1.getT().start();
		 for(int i = 0;i<5;i++)
		 {
			 System.out.println("Main thread : "+i);
			 Thread.sleep(300);
		 }
	}

}
