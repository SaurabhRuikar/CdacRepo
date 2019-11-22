package database;

import java.sql.Connection;

import java.sql.DriverManager;
import java.sql.PreparedStatement;

import java.util.Scanner;

public class StatementApp 
{

	public static void main(String[] args) throws Exception
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
		
		Scanner sc = new Scanner(System.in);

		System.out.println("Enter EmpId : ");
		int emp_id = sc.nextInt();
		System.out.println("Enter name : ");
		String ename = sc.next();
		System.out.println("Enter sal : ");
		int sal = sc.nextInt();
		
		PreparedStatement ps = con.prepareStatement("insert into emp values(?,?,?)");
		
		ps.setInt(1, emp_id);
		ps.setString(2, ename);
		ps.setInt(3, sal);
		
		
		
		int i = ps.executeUpdate();
		
		System.out.println(i+" data inserted");
		
		con.close();
		ps.close();
	}

}
