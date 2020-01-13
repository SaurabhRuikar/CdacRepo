package org.cdac.MapreducePartitioner;

import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Partitioner;


public class MyPartioner extends Partitioner<Text, Text> 
{

	@Override
	public int getPartition(Text arg0, Text arg1, int arg2) 
	{
		String [] values = arg1.toString().split(",");
		if(values[0].equalsIgnoreCase("IT"))
		{
			return 0;
		}
		else if(values[0].equalsIgnoreCase("Admin"))
		{
			return 1;
		}
		else if(values[0].equalsIgnoreCase("Finane"))
		{
			return 2;
		}
		else
		{
			return 3;
		}
		
	}

}
