package org.cdac.org.assignment4;

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
	
			 String line = value.toString();
			 String [] values = line.split("[|]");
			 String shipvia = values[6];
			 context.write(new Text(shipvia), new IntWritable(1));
		
	}

}
