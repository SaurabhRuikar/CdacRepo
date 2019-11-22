import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class QuizQuestions {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Connection con=null;
		Statement st=null;
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3307/quizdb","root","");
			st=con.createStatement();
			ResultSet rs=st.executeQuery("Select t.name,count(t.topicid) from questions q,topics t where q.topicid=t.topicid group by t.topicid");
			while(rs.next())
			{
				System.out.print("Topic Name :"+rs.getString(1)+"\t\t\t");
				System.out.print("No of Questions :"+rs.getInt(2)+"\t\t\t");
				
				System.out.println();
			}
			rs.close();
			st.close();
			con.close();
			
		}
		catch (Exception e) {
			e.printStackTrace();
		}
		
		
	}

}
