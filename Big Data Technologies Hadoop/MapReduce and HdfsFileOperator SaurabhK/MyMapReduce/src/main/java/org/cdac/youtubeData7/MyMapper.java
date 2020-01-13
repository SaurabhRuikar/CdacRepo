package org.cdac.youtubeData7;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class MyMapper extends Mapper<LongWritable, Text, Text, FloatWritable>
{

	

	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, FloatWritable>.Context context)
			throws IOException, InterruptedException 
	{
		try
		{
			
            String line = value.toString();
			 String [] values = line.split("\t");
			 String id = values[0];
			 String category=values[3];
			 int rating = Integer.parseInt(values[6]);
			 context.write(new Text(category) , new FloatWritable(rating));
		}

		catch(Exception e)
		{
			
		}
	}

}
