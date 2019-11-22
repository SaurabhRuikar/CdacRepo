package database;

import java.awt.Window.Type;
import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Types;
import java.util.Scanner;

public class StoredProcedure 
{

	public static void main(String[] args) throws ClassNotFoundException, SQLException 
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the id : ");
		int id = sc.nextInt();
		CallableStatement c = con.prepareCall("{call getID(?,?,?)}");
		c.setInt(1, id);
		
		c.registerOutParameter(2, Types.VARCHAR);
		c.registerOutParameter(3, Types.VARCHAR);

		c.execute();
		
		System.out.println("Name : "+c.getString(2)+"  Salary : "+c.getInt(3));
	}

}
