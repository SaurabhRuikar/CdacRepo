package org.cdac.youtubeData6;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, NullWritable, IntWritable>
{

	

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, NullWritable, IntWritable>.Context context)
			throws IOException, InterruptedException 
	{
		try
		{
			
            String line = value.toString();
			 String [] values = line.split("\t");
			 String id = values[0];
			 int views = Integer.parseInt(values[5]);
			 context.write(NullWritable.get() , new IntWritable(views));
		}

		catch(Exception e)
		{
			
		}
	}

}
