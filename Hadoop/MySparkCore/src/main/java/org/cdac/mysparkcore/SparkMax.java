package org.cdac.mysparkcore;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class SparkMax {

	public static void main(String[] args) 
	{
		
		JavaSparkContext context = new JavaSparkContext("local[*]", "MaxSalary");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> lines1 = lines.filter(new Function<String, Boolean>() 
		{
			
			@Override
			public Boolean call(String v1) throws Exception {
				// TODO Auto-generated method stub
				return !v1.contains("Salary");
			}
		});
		JavaPairRDD<String, Integer> salTuple = lines1.mapToPair(new PairFunction<String, String, Integer>() 
		{
			@Override
			public Tuple2<String, Integer> call(String t) throws Exception
			{
					String []words = t.split(",");
					int salary = Integer.parseInt(words[4]);
					return new Tuple2<String, Integer>(words[3], salary);
			}
			
			
		});
		
		JavaPairRDD<String, Integer> max = salTuple.reduceByKey(new Function2<Integer, Integer, Integer>() {
			
			@Override
			public Integer call(Integer v1, Integer v2) throws Exception 
			{
				if(v1 > v2)
				{
					return v1;
				}
				else
					return v2;
			}
		});
		
		max.foreach(new VoidFunction<Tuple2<String,Integer>>() {
			
			@Override
			public void call(Tuple2<String, Integer> t) throws Exception 
			{
				// TODO Auto-generated method stu
				System.out.println(t._1+" : "+t._2);
				
			}
		});
	}

}
