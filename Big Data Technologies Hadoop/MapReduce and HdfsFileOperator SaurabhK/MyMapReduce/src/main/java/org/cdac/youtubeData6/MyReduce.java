package org.cdac.youtubeData6;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<NullWritable, IntWritable, Text, IntWritable>
{
	@Override
	protected void reduce(NullWritable arg0, Iterable<IntWritable> arg1,
			Reducer<NullWritable, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException 
	{	
		int max = 0;
		for(IntWritable t1:arg1)
		{
			int val=t1.get();
			
			if(val>max)
			{
				max = val;
				
			}
			
		}
		
		
		
		arg2.write(new Text("Max : "), new IntWritable(max));
	}
}
