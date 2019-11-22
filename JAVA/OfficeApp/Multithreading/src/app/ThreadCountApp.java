package app;

import multithreading.ThreadCount;

public class ThreadCountApp {

	public static void main(String[] args) throws InterruptedException 
	{
		System.out.println("Starting to count......");
		ThreadCount t1 = new ThreadCount(100, "First");
		ThreadCount t2 = new ThreadCount(50, "Second");
		ThreadCount t3 = new ThreadCount(200, "Third");
		
		t1.getT().start();
		t2.getT().start();
		t3.getT().start();
		
		t1.getT().join();
		t2.getT().join();
		t3.getT().join();
		
		System.out.println("End of count......");
	}

}
