package Collection;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;



public class CollectionDemo {

	public static void main(String[] args) throws FileNotFoundException, IOException {
		// TODO Auto-generated method stub

		
		List<String> l= new ArrayList<String>();
		l.add("vishal");
		l.add("ankit");
		l.add("kunal");
		
		for(String s:l)
		{
			
			System.out.println(s);
			
		}
		
		ObjectOutputStream oos=new ObjectOutputStream(new FileOutputStream("/home/student/Desktop/name.txt"));
		for(String s:l)
		{
			oos.writeObject(s);
			
		}
		oos.close();	
		
	}

}
