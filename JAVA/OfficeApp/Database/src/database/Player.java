package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class Player {

public static void main(String[] args) {
		

		Connection con=null;
		Statement st=null;
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3307/test","root","");
			st=con.createStatement();
			ResultSet rs=st.executeQuery("Select * from player p, player_score pl where p.id=pl.id order by pl.score desc   ");
			while(rs.next())
			{
				System.out.println("player id :"+rs.getInt(1));
				System.out.println("name :"+rs.getString(2));
				System.out.println("player id :"+rs.getInt(3));
				System.out.println("Match id :"+rs.getInt(4));
				System.out.println("Score :"+rs.getInt(5));
				System.out.println("average :"+(rs.getInt(5) )/ (rs.getInt(4)));
				System.out.println("====================================");
			}
			rs.close();
			st.close();
			con.close();
			
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		

	}

}
