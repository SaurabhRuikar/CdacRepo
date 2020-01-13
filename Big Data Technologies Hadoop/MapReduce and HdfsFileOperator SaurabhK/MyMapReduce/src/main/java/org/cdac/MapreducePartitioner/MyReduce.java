package org.cdac.MapreducePartitioner;

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
		/*int max = 0;
		for(Text i : arg1)
		{
			String [] values = i.toString().split(",");
			int val = Integer.parseInt(values[1]);
			if(val > max)
			{
				max = val; 
			}
		}
		
		int sum = 0,cnt = 0;
		for(IntWritable i : arg1)
		{
			sum += i.get();
			cnt++;
		}
		int avg = sum/cnt;
		*/
		
		int min = Integer.MAX_VALUE;
		for(Text i : arg1)
		{
			String [] values = i.toString().split(",");
			int val = Integer.parseInt(values[1]);
			if(val < min)
			{
				min = val; 
			}
		}
		
		arg2.write(arg0, new IntWritable(min));
	}
}
