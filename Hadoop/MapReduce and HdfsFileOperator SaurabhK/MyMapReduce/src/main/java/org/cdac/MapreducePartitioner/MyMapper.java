package org.cdac.MapreducePartitioner;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MyMapper extends Mapper<LongWritable, Text, Text, Text>
{

	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException 
	{
		try
		{
			 String line =value.toString();
			 String [] values=line.split(",");
			 String gender=values[3];
			 int salary=Integer.parseInt(values[4]);
			 context.write(new Text(gender), new Text(values[1]+","+values[4]));
		}
		catch(Exception e)
		{
			e.printStackTrace(); 
		}
	}

}
