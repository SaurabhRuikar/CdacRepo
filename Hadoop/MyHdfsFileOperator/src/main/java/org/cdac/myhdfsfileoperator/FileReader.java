package org.cdac.myhdfsfileoperator;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;

import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.LocatedFileStatus;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.fs.RemoteIterator;

public class FileReader {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		FileSystem fs= FileSystem.get(new Configuration());
		/*
		FileSystem fs= FileSystem.get(new Configuration());
		InputStream in= fs.open(new Path(args[0]));
		IOUtils.copy(in, System.out);
		*/
		
		/*OutputStream out= fs.create(new Path(args[0]));
		out.write("Hiiiiiiii".getBytes());
		out.close();*/
		
		RemoteIterator<LocatedFileStatus> ri=fs.listFiles(new Path(args[0]), true);
		while(ri.hasNext())
		{
			System.out.println(ri.next().getPath().getName());
			
		}
		
		/*
		fs.mkdirs(new Path(args[0]));	
		*/

	}
	

}
