package threadapps;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class ReadThreadDemo {

	public static void main(String[] args) throws IOException, InterruptedException {
		// TODO Auto-generated method stub
		System.out.println("Enter the path of the file");
		Scanner sc=new Scanner(System.in);
        String path=sc.next();
        BufferedReader br=new BufferedReader(new FileReader(path));
        
        
        System.out.println("Enter the path of the file");
		Scanner sc1=new Scanner(System.in);
        String path0=sc.next();
        BufferedReader br1=new BufferedReader(new FileReader(path0));
        
        System.out.println("Enter the path of the file");
		Scanner sc2=new Scanner(System.in);
        String path7=sc.next();
        BufferedReader br2=new BufferedReader(new FileReader(path7));
        
        
        
        
        
        
        
        ReadThread r1=new ReadThread(br);
       ReadThread r2=new ReadThread(br1);
      ReadThread r3=new ReadThread(br2);
        
        r1.getT().start();
      r2.getT().start();
       r3.getT().start();
        
        r1.getT().join();
       r2.getT().join();
        r3.getT().join();
        
        
       br.close();
       br1.close();
       br2.close();
     
        

	}

}
