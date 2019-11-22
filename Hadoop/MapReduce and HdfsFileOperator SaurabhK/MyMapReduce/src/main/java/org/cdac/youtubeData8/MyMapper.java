package org.cdac.youtubeData8;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, Text, IntWritable>{
	
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {
	
		try {
			String line=value.toString();
			String[] val=line.split("\t");
			String uploader=val[1];
			int v=Integer.parseInt(val[5]);
			
				context.write(new Text(uploader) ,new IntWritable(v));
		
			}
	catch(Exception e)
	{
		
	}
	}

}
