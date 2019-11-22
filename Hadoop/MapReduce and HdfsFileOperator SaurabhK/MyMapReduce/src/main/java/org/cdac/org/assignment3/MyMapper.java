package org.cdac.org.assignment3;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, Text, Text>
{

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException 
	{
	
			 String line = value.toString();
			 String [] values = line.split("[|]");
			 String country = values[8];
			 if(country.contains("Brazil"))
			 {	 
				 context.write(new Text("country"), new Text(country));
			 }
		
	}

}
