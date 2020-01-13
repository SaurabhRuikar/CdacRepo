package org.cdac.MyMapReduce;

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
			 String line =value.toString();
			 String [] values=line.split(",");
			 String gender=values[3];
			 int salary=Integer.parseInt(values[4]);
			 context.write(new Text(gender), new IntWritable(salary));
		}
		catch(Exception e)
		{
			
		}
	}

}
