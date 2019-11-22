import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Types;
import java.util.Scanner;

public class QuizProcedure {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {
		// TODO Auto-generated method stub
		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/quizdb", "root", "");
	
		CallableStatement c = con.prepareCall("{call getquiz }");
		ResultSet rs = c.executeQuery();
		while(rs.next())
		{
			System.out.print("Topic name="+rs.getString(1));
			System.out.println();
			System.out.println("Questions="+rs.getInt(2));
			
		}
		
		
		
	}

}
