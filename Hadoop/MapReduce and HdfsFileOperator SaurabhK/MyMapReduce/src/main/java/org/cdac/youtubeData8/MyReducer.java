package org.cdac.youtubeData8;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
	
	int max=0;
	String str=null;
	
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1, Reducer<Text, IntWritable, Text, IntWritable>.Context arg2)
			throws IOException, InterruptedException {
		
		int cnt=0;
		for(IntWritable ag: arg1)
		{
			int curval=ag.get();
			cnt++;
			
		}
		if(cnt>max)
		{
			str=arg0.toString();
			max=cnt;
		}
		
		//	arg2.write(arg0,new IntWritable(cnt))			
	}

	@Override
	protected void cleanup(Reducer<Text, IntWritable, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
		
		context.write(new Text(str),new IntWritable(max));
	}
	

}
