package org.cdac.MyMapReduce;

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
		/*int max = 0;
		for(IntWritable i : arg1)
		{
			int val = i.get();
			if(val > max)
			{
				max = val; 
			}
		}*/
		
		int sum = 0,cnt = 0;
		for(IntWritable i : arg1)
		{
			sum += i.get();
			cnt++;
		}
		int avg = sum/cnt;

		
		
		arg2.write(arg0, new IntWritable(avg));
	}
}
