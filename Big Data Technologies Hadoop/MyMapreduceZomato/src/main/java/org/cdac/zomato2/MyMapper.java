package org.cdac.zomato2;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, Text, Text>
{

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException 
	{
		try
		{
			
            String line = value.toString();
			 String [] values = line.split("[,\"]");
			 String rname=values[1];
			 String booking = values[12];
			 int id = Integer.parseInt(values[0]);
			 context.write(new Text(rname), new Text(booking));
		}

		catch(Exception e)
		{
			
		}
	}

}
