package database;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Types;

public class InOutDatabase {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// TODO Auto-generated method stub
		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");  
		CallableStatement cs =con.prepareCall("{call sal(?)}");
		
		cs.setInt(1, 3);
		cs.registerOutParameter(1,Types.INTEGER);
		cs.execute();
	System.out.println("salary  :"+cs.getInt(1));

		
	}

}
