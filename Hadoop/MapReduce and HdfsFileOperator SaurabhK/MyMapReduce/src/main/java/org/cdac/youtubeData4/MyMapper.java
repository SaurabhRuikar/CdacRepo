package org.cdac.youtubeData4;

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
			
            String line = value.toString();
			 String [] values = line.split("\t");
			 String category = values[3];
			 int views = Integer.parseInt(values[5]);
			 context.write(new Text(category), new IntWritable(views));
		}

		catch(Exception e)
		{
			
		}
	}

}
