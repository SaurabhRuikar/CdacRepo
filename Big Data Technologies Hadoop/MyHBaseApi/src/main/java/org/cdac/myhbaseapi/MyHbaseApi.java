package org.cdac.myhbaseapi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;


import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;

public class MyHbaseApi {

	public static void main(String[] args) throws Exception 
	{
		
		MyHbaseApi m = new MyHbaseApi();
		
		Scanner sc = new Scanner(System.in);
		FileSystem fs = FileSystem.get(new Configuration());
		
		Configuration con= HBaseConfiguration.create();
		con.setInt("hbase.zookeeper.property.clientPort", 2222);
		HTable hTab = new HTable(con, "youtube1");
		
		InputStream in = fs.open(new Path("/youtubedata.csv"));
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		String str = "";
		while((str = br.readLine()) != null)
		{
			try
			{
				String [] values = str.split(",");
				
				m.writes(values[0], "uploader", values[1], hTab);
	
				m.writes(values[0], "interval", values[2], hTab);
			
				m.writes(values[0], "category", values[3], hTab);
				
				m.writes(values[0], "length", values[4], hTab);
				
				m.writes(values[0], "views", values[5], hTab);
			
				m.writes(values[0], "rating", values[6], hTab);
				
				m.writes(values[0], "ratings", values[7], hTab);
				
				m.writes(values[0], "comments", values[8], hTab);
			}
			catch(Exception e)
			{
				
			}
		}
		hTab.flushCommits();
		hTab.close();
		
	}
	
	public void writes(String id, String col, String val,HTable hTab) throws IOException
	{
		Put put = new Put(id.getBytes());
		put.add("data".getBytes(),col.getBytes(), val.getBytes());	
		hTab.put(put);
	}

}
