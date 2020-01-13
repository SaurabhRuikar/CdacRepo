package org.cdac.mymapreduce;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, Text, IntWritable> 
{
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException
	{
		
		try 
		{
			
		
			String line=value.toString();
			String[] s= line.split(",");
			String gender=s[3];
			int salary=Integer.parseInt(s[4]);
			context.write(new Text(gender), new IntWritable(salary));
		}
		
		catch(NumberFormatException e)
		{
			
		}
		
		
	}
}
