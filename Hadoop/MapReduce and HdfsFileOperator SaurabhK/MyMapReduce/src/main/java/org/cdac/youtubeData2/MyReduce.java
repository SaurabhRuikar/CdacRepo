package org.cdac.youtubeData2;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReduce extends Reducer<Text, IntWritable, Text, Text>
{
	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, Text>.Context arg2) throws IOException, InterruptedException 
	{	
		arg2.write(arg0, new Text(" "));
	}
}
