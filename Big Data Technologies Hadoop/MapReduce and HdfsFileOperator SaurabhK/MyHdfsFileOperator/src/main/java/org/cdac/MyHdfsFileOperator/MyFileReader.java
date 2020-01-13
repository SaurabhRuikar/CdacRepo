package org.cdac.MyHdfsFileOperator;

import java.io.InputStream;
import java.io.OutputStream;
import java.util.Scanner;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;

public class MyFileReader 
{

	public static void main(String[] args) throws Exception
	{
		
		Scanner sc = new Scanner(System.in);
		FileSystem fs = FileSystem.get(new Configuration());
		String c = "/";
		int x = 1;
		while(x == 1)
		{
			System.out.println("Menu  \n1.Read\n2.Create\n3.Delete\n4.Write\n5.Listfiles");
			System.out.println("Enter your choice");
			int ch = sc.nextInt();
			
			switch (ch) 
			{
				case 1:	
					System.out.println("Enter file name to read");
					String path = sc.next();
					path = c.concat(path);
					InputStream in = fs.open(new Path(path));
					org.apache.commons.io.IOUtils.copy(in, System.out);
					in.close();
					break;
				case 2:
					System.out.println("Enter the path of the file");
					String path1 = sc.next();
					path1 = c.concat(path1);
					fs.create(new Path(path1));
					System.out.println("File is created");
					break;
				case 3:
					System.out.println("Enter the file name to delete");
					String path2 = sc.next();
					path2 = c.concat(path2);
					fs.delete(new Path(path2));
					break;
				case 4:
					String wr = "Vishal is a good boy";
					System.out.println("Enter the file name to write in");
					String f = sc.next();
					f = c.concat(f);
					OutputStream out = fs.create(new Path(f));
					out.write(wr.getBytes());
					System.out.println();
					out.close();
					break;
				case 5:
					System.out.println("Enter the file path");
					String path3 = sc.next();
					path3=c.concat(path3);
					RemoteIterator <LocatedFileStatus> i = fs.listFiles(new Path(path3), true);
					while(i.hasNext())
					{
						System.out.println(i.next());
					}
					break;
					
				default:
					System.out.println("Exiting !!!!");
					x = 0;
					break;
			}
			fs.close();
			sc.close();
		}

	}

}
