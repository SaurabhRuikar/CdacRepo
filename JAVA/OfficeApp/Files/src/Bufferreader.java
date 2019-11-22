import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;


public class Bufferreader {

	public static void main(String[] args) throws IOException 
	{
		BufferedReader br = new BufferedReader(new FileReader("/home/student/Desktop/new.txt"));
		String str;
		int cnt=1;
		while((str=br.readLine())!=null)
				{
			
					System.out.println((cnt++)+". "+str);
			
				}
		br.close();
		
		
	}

}
