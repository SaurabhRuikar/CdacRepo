package assignment;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

public class MarksDemo {

	public static void main(String[] args) throws IOException {
		
		File f=new File("/home/student/Desktop/marks.csv");
		BufferedReader br=null;
		Set<String> b=new TreeSet<>(new Comparator<String>() {

			@Override
			public int compare(String o1, String o2) {
				
				String i1[]=o1.split(" ");
				String i2[]=o2.split(" ");
				
				
				return Integer.parseInt(i2[2])-Integer.parseInt(i1[2]);
			}
			
		});
		br=new BufferedReader(new FileReader(f));
		if(f.exists())
		{
			if(f.canRead())
			{
				
				String i;
				while((i=br.readLine())!= null)
				{
					int marks=0;
					String i1[]=i.split(",");
					for(int l=2;l<i1.length;l++)
					{
						marks+=Integer.parseInt(i1[l]);
					}
					
					b.add(i1[0]+" "+i1[1]+" "+Integer.toString(marks));
					
				}
				
			}
		}
		
		for(String s:b)
		{
			
			System.out.println(s);
		}
		
		
	}
}

