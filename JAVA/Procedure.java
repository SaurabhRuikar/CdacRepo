import java.sql.CallableStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Types;
import java.util.Scanner;

public class Procedure {

	public static void main(String[] args) throws ClassNotFoundException, SQLException 
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/customer", "root", "");
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the id : ");
		String custid = sc.nextLine();
		CallableStatement c = con.prepareCall("{call getInfo(?,?,?)}");
		c.setString(1, custid);
		
		c.registerOutParameter(2, Types.VARCHAR);
		c.registerOutParameter(3, Types.VARCHAR);

		c.execute();
		
		System.out.println("Name : "+c.getString(2)+"  Contact : "+c.getString(3));
	}

}
