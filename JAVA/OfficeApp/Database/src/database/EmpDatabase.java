package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class EmpDatabase 
{

	public static void main(String[] args) throws Exception
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3307/company","root","");
		Statement st=con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_UPDATABLE);
		
		ResultSet rs = st.executeQuery("select * from emp");
		while(rs.next())
		{
			if(rs.getInt(3)<1000)
			{
				rs.updateInt(3, (int)((float)rs.getInt(3)*1.02));
				rs.updateRow();
			}
			if(rs.getInt(3)>=1000 && rs.getInt(3)<20000)
			{	
				rs.updateInt(3, (int)((float)rs.getInt(3)*1.05));
				rs.updateRow();
			}
			if(rs.getInt(3)>=20000 && rs.getInt(3)<50000)
			{
				rs.updateInt(3, (int)((float)rs.getInt(3)*1.07));
				rs.updateRow();
			}
			if(rs.getInt(3)>=50000)
			{
				rs.updateInt(3, (int)((float)rs.getInt(3)*1.08));
				rs.updateRow();
			}
		}
		System.out.println("Updated");
		
		

	}

}
