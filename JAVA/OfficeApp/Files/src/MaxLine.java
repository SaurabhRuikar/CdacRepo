import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class MaxLine 
{

	public static void main(String[] args) throws IOException 
	{
		BufferedReader br = new BufferedReader(new FileReader("/home/student/Desktop/games.json"));
		String str;
		
		MaxLen []m = new MaxLen[34];
		int i=0;
		int max = 0;
		while((str=br.readLine())!=null)
		{
			m[i++] = new MaxLen(str.length(), str);
		}
		
		for(MaxLen n : m)
		{
			//System.out.println(n);
			
			if(n.a > max)
			{
				max = n.a;
			}
		}
		for(MaxLen n : m)
		{
			//System.out.println(n);
			if(n.a == max)
			{
				System.out.println(n);
			}
		}
		
		br.close();
	}


}
