package Assignment;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class DisplayFileCall {

	public static void main(String[] args) throws IOException, InterruptedException {
		String filePath;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter file path");
		filePath=sc.nextLine();
		BufferedReader br=new BufferedReader(new FileReader(filePath));
		DisplayFile r=new DisplayFile(br);
		DisplayFile r1=new DisplayFile(br);
		DisplayFile r2=new DisplayFile(br);
		r.getT().start();
		r.getT().join();
		r1.getT().start();
		r1.getT().join();
		r2.getT().start();
			
	
		
		r2.getT().join();
		br.close();
	}

}