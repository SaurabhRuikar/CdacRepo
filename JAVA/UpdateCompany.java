import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class UpdateCompany {

	public static void main(String[] args) throws SQLException, ClassNotFoundException {
		// TODO Auto-generated method stub
		Class.forName("com.mysql.jdbc.Driver");
		Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3307/company", "root", "");
		
		Statement stmt = con.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_UPDATABLE);
	
	    ResultSet rs=stmt.executeQuery("Select empid,salary from emp");
	    while(rs.next())
	    {
	    	System.out.println(rs.getInt(1));
	    	System.out.println(rs.getFloat(2));
	    	if(rs.getFloat(2)<10000)
		    {
	    		float s= rs.getFloat(2)+rs.getFloat(2)*2/100;
		    	rs.updateFloat(2,s);
		    	rs.updateRow();
		    	
		    }
	    	if(rs.getFloat(2)>10000 && rs.getFloat(2)<20000)
		    {
	    		float p= rs.getFloat(2)+rs.getFloat(2)*5/100;
		    	rs.updateFloat(2,p);
		    	rs.updateRow();
		    	
		    }
	    	if(rs.getFloat(2)>=20000 && rs.getFloat(2)<50000)
			{	
				float q= rs.getFloat(2)+rs.getFloat(2)*7/100;
				rs.updateFloat(2,q);
				rs.updateRow();
			}
	    	if(rs.getFloat(2)>=50000)
	    	{
	    		float r = rs.getFloat(2)+rs.getFloat(2)*8/100;
	    		rs.updateFloat(2, r);
	    		rs.updateRow();
	    	}
	    	System.out.println("The Salary has been updated Successfully... ");
			
	    }
	    
		
		
			
		
	}

}
