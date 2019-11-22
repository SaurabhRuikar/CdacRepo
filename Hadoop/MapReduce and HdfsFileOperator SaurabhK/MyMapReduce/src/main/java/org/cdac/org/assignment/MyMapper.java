package org.cdac.org.assignment;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.yarn.webapp.hamlet.Hamlet.MAP;

public class MyMapper extends Mapper<LongWritable, Text, Text, IntWritable>
{
 
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException 
	{
		try
		{
			 String line = value.toString();
			 String [] values = line.split("[|]");
			 String empid = values[2];
			 context.write(new Text(empid), new IntWritable(1));
		}
		catch(Exception e)
		{
			
		}
	}

}
