package org.cdac.youtubeData4;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<Text, IntWritable, Text, IntWritable>
{
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException 
	{	
		int max=0;
		for(IntWritable t1:arg1)
		{
			int val=t1.get();
			
			if(val>max)
			{
				max=val;
				
			}
			
		}
		
		
		
		arg2.write(arg0, new IntWritable(max));
	}
}
