import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class bufferrenfilewrite {

	public static void main(String[] args) throws IOException {

		
		BufferedReader br = new BufferedReader(new FileReader("/home/student/Desktop/sql.java"));
       BufferedWriter fi=new BufferedWriter(new FileWriter("/home/student/Desktop/file.txt"));
       
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
