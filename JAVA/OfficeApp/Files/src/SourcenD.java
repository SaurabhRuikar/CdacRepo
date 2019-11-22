import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class SourcenD extends Exception {

	public static void main(String[] args) throws IOException {


		BufferedReader b= new BufferedReader(new InputStreamReader(System.in));
		System.out.println("enter path for reading");
		String path1=b.readLine();
		System.out.println("enter path for writing");
		String path2=b.readLine();


		BufferedReader br = new BufferedReader(new FileReader(path1));
		BufferedWriter fi=new BufferedWriter(new FileWriter(path2));

		String str;
		while((str=br.readLine())!=null)
		{
			fi.write(str);
			fi.newLine();


		}

		br.close();
		fi.close();


	}

}
