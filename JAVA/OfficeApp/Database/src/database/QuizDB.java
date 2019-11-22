package database;

import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Types;

public class QuizDB {

	public static void main(String[] args) throws Exception
	{
		Class.forName("com.mysql.jdbc.Driver");
		Connection con=DriverManager.getConnection("jdbc:mysql://localhost:3307/quizdb","root","");
		Statement st=con.createStatement();
		ResultSet rs = st.executeQuery("select t.name,count(*) from questions q,topics t where q.topicid=t.topicid group by t.name");

		while(rs.next())
		{
			System.out.println(rs.getString(1)+" : "+rs.getInt(2));
		}
		
		
		System.out.println("=========================================");
	/*	
		CallableStatement c = con.prepareCall("{call GetQue()}");
		
		boolean flag = c.execute();
		while(flag)
		{
			ResultSet rs1 = c.getResultSet();
			while(rs1.next())
			{
				System.out.println("name : "+rs1.getString(1)+" : "+rs1.getInt(2));
			}
			
			flag=rs1.next();
		}
*/		
	
	}

}
