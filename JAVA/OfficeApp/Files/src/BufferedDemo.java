
	import java.io.BufferedWriter;
	import java.io.FileWriter;
	import java.io.IOException;


public class BufferedDemo  {
	

		public static void main(String[] args)
		{
			BufferedWriter bw;
			
			try
			{
				bw=new BufferedWriter(new FileWriter("/home/student/new.txt")); 
				
				bw.write("hello");
				bw.newLine();
				bw.write("hi");
				bw.newLine();
				bw.flush();
				bw.close();
				
				
			}
			catch (IOException e)
			{
				
			}
			
		}

	}


