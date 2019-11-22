package Assignment;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class DivisorThread {
  
	
	public static void main(String[] args) throws InterruptedException, IOException {
		
		
		Scanner sc =new Scanner(System.in);
		System.out.println("enter the number ");
		int num=sc.nextInt();
		int num1=sc.nextInt();
		int num2=sc.nextInt();
		FileWriter fw=new FileWriter("/home/student/Desktop/divisor.txt");
		
		//System.out.println("Divisors of "+num+" are : ");
		 DivisorThread1 t = new DivisorThread1(num,fw);
		 
		 DivisorThread1 t1 = new DivisorThread1(num1,fw);
		 DivisorThread1 t2 = new DivisorThread1(num2,fw);
		
		 t.getT().start();
		 t1.getT().start();
		 t2.getT().start();
		 
		 t.getT().join();
		 t1.getT().join();
		 t2.getT().join();
		 fw.close();
		 
		 
		 
		
	}

}
