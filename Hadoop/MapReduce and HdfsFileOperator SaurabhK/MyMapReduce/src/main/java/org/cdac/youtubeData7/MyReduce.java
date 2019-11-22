package org.cdac.youtubeData7;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<Text, FloatWritable, Text, FloatWritable>
{
	@Override
	protected void reduce(Text arg0, Iterable<FloatWritable> arg1,
			Reducer<Text, FloatWritable, Text, FloatWritable>.Context arg2) throws IOException, InterruptedException 
	{	
		float avg = 0,cnt = 0,sum = 0;
		for(FloatWritable t1:arg1)
		{
			float val=t1.get();
			sum += val;
			cnt++;
		}
		
		avg = sum/cnt;
		
		
		arg2.write(new Text(arg0), new FloatWritable(avg));
	}
}
