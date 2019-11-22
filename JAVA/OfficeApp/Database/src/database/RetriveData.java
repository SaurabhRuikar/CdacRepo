package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

import collection.Emp;

public class RetriveData {

	public static void main(String[] args) throws Exception
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
		
		Scanner sc = new Scanner(System.in);
		Set<Emp> e = new HashSet<>();
		
		Statement s = con.createStatement();
		ResultSet r = s.executeQuery("select * from emp");
		
		while(r.next())
		{
			e.add(new Emp(r.getInt(1), r.getString(2), r.getInt(3)));
		}
	
		System.out.println("Enter EmpId : ");
		int emp_id = sc.nextInt();
		PreparedStatement st=con.prepareStatement("Select emp_id from emp where emp_id=?");
		st.setInt(1, emp_id);
		ResultSet rs=st.executeQuery();
		while(rs.next())
		{
			if(rs.getInt(1)==emp_id)
			{
				System.out.println("Id is already present please enter another id");
				emp_id=sc.nextInt();
			}
		}
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
