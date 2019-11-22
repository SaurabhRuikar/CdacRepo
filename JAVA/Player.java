package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.Scanner;

public class Player {

	public static void main(String[] args) throws Exception
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
		PreparedStatement ps=null;
		Scanner sc = new Scanner(System.in);
		String ans="";
		do
		{
		System.out.println("Enter Id : ");
		int id = sc.nextInt();
		System.out.println("Enter Name : ");
		String name = sc.next();
		System.out.println("Enter MatchId : ");
		int match_id = sc.nextInt();
		System.out.println("Enter Score : ");
		int score = sc.nextInt();
		
		ps = con.prepareStatement("insert into player values(?,?,?,?)");
		
		ps.setInt(1, id);
		ps.setString(2, name);
		ps.setInt(3, match_id);
		ps.setInt(4, score);
				
		int i = ps.executeUpdate();
		
		System.out.println(i+" data inserted");
		System.out.println("Do you want to continue : ");
		ans = sc.next();
		}while(ans.equals("y"));
		con.close();
		ps.close();
	}

}
