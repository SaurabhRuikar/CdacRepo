import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class lensimple {

	

	public static void main(String[] args)throws IOException {
		
		BufferedReader br=null;
		br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("enter path");
		String file1=br.readLine();
		
		File f=new File(file1);
		
		if(f.exists())
		{
			if(f.canRead())
			{
					br=new BufferedReader(new FileReader(f));
					 
					String i,k="";
					
					
					int j=0,max=0;
					while((i=br.readLine())!= null)
					{
						
						if(i.length()>max)
						{
							k=i;
							max=i.length();
						}
						
					}
					System.out.println(k);
					System.out.println(k.length());
					br.close();
					
					
				}
			}
		
		}
		

}
