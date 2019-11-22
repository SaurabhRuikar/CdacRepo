package org.cdac.zomato2;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<Text, Text, Text, Text>
{
	@Override
	protected void reduce(Text arg0, Iterable<Text> arg1,
			Reducer<Text, Text, Text, Text>.Context arg2) throws IOException, InterruptedException 
	{	
		
		String rname = "";
		for(Text t : arg1)
		{
			//rname = arg1.toString()
			if(arg1.toString().equalsIgnoreCase("Yes"))
			{
				arg2.write(arg0, new Text("yes"));
			}
		}

		
		
		
		
		
	
	}
}
