package org.cdac.org.assignment3;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<Text, Text, Text, IntWritable>
{
	@Override
	protected void reduce(Text arg0, Iterable<Text> arg1,
			Reducer<Text, Text, Text, IntWritable>.Context arg2) throws IOException, InterruptedException 
	{
		int cnt = 0;
		
		for(Text t : arg1)
		{
			cnt++;
			
		}
		
		
		arg2.write(arg0, new IntWritable(cnt));
	}
}
