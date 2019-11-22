package org.cdac.youtubeData3;

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
		int avg = 0,count = 0,sum = 0;
		for(IntWritable t1:arg1)
		{
			sum = sum+t1.get();
			count++;
			
		}
		
		 avg=sum/count;
		
		arg2.write(arg0, new IntWritable(avg));
	}
}
