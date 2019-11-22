package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Comparator;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

import collection.Emp;

public class DataTree {

	public static void main(String[] args) throws Exception
	{

		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/test", "root", "");
		
		Scanner sc = new Scanner(System.in);
		Set<Emp> e = new TreeSet<>(new Comparator<Emp>() {

			@Override
			public int compare(Emp o1, Emp o2) {
				// TODO Auto-generated method stub
				return o1.getEname().compareTo(o2.getEname());
			}
		});
		
		Statement s = con.createStatement();
		ResultSet r = s.executeQuery("select * from emp");
		
		while(r.next())
		{
			e.add(new Emp(r.getInt(1), r.getString(2), r.getInt(3)));
		}
	
		for(Emp e1 : e)
		{
			System.out.println(e1);
		}
		
		con.close();
	}

}
