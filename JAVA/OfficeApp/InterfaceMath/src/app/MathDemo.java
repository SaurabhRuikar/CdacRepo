package app;

import java.util.Scanner;

import math.MathClass;

public class MathDemo {

	public static void main(String[] args) {
		
		
		Scanner sc= new Scanner(System.in);
		MathClass m =new MathClass();
		System.out.print("Enter the no : ");
		int p = sc.nextInt();
		System.out.println(p+" is prime : "+m.isPrime(p));
		
		//System.out.print("Enter the no : ");
		//int q = sc.nextInt();
		System.out.println(p+" is palindrome : "+m.isPallindrom(p));
		
		//System.out.print("Enter the no : ");
		//int r = sc.nextInt();
		System.out.println("Factorial is : "+m.getFactorial(p));
	}

}
