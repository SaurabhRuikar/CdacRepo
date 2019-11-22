package org.cdac.mymapreduce;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class MyReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

	@Override
	protected void reduce(Text arg0, Iterable<IntWritable> arg1,
			Reducer<Text, IntWritable, Text, IntWritable>.Context arg2) throws IOException, InterruptedException {
	/*
	 int max=0;
	 for(IntWritable value:arg1)
	 {
		 int intvalue=value.get();
		 if(intvalue > max)
		 {
			 max=intvalue;
		 }
		 
	 }
	 
	 arg2.write(arg0, new IntWritable(max));
	*/
	/*
	int sum=0;
	for(IntWritable value:arg1)
	{ 
		int intvalue=value.get();
		sum=sum+intvalue;
	}
	 arg2.write(arg0, new IntWritable(sum));

	
	}
	*/
		
		int avg=0,sum=0,count=0;
		for(IntWritable value:arg1)
		{ 
			int intvalue=value.get();
			sum=sum+intvalue;
			count=count+1;
			
		}
			avg=sum/count;
		 arg2.write(arg0, new IntWritable(avg));
		
		
		
	
}
}
