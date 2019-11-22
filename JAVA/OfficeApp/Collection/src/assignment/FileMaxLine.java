package assignment;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;



public class FileMaxLine 
{

	public static void main(String[] args) throws IOException 
	{
		BufferedReader br = new BufferedReader(new FileReader("/home/student/Desktop/hello.txt"));
		String str;
		Set<String> s = new TreeSet<>(new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				// TODO Auto-generated method stub
				
				return o2.length() - o1.length();
			
			}
		});
		
		int max = 0;
		while((str=br.readLine())!=null)
		{
			s.add(str);
		}
		for(String s1 : s)
		{
			System.out.println(s1.length()+" : "+s1);
			System.out.println("");				
		}
		
		//System.out.println(max+" : "+k);
		
		br.close();
	}

}
