package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Scrollableupdate {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// TODO Auto-generated method stub

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
	  Statement stm = con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_UPDATABLE);
	  ResultSet res=stm.executeQuery("select *from emp");
	  res.last();
	  System.out.println("record number : "+res.getRow());
	  res.afterLast();
	  while(res.previous())
	  {
		  System.out.println(res.getInt(1)+" : "+res.getString(2));
		  
	  }
	  res.absolute(3);
	  System.out.println(+res.getInt(1)+" : "+res.getString(2));
	  res.updateString(2, "saurabh100000000");
	  res.updateRow();
	 System.out.println("row updated");
	  
	}

}
