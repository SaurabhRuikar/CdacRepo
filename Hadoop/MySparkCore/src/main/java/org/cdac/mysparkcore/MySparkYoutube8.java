package org.cdac.mysparkcore;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkYoutube8 
{
	
public static void main(String[] args)
	
	
	{
		JavaSparkContext context = new JavaSparkContext("local[*]", "avg");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> lines1= lines.filter(new Function<String, Boolean>() {

			@Override
			public Boolean call(String v1) throws Exception {
				// TODO Auto-generated method stub
				return v1.contains("\t");
			}
		
		});
		
		
		
		JavaPairRDD<String,Integer> wordTuple = lines1.mapToPair(new PairFunction<String, String, Integer>() 
		{

			@Override
			public Tuple2<String, Integer> call(String t) throws Exception {
				String [] words = t.split("\t");
				return new Tuple2<String, Integer>(words[1],1);
			}
		});
		
		wordTuple.reduceByKey(new Function2<Integer, Integer, Integer>() 
		{
			
			@Override
			public Integer call(Integer v1, Integer v2) throws Exception {
				// TODO Auto-generated method stub
				return v1+v2;
			}
		}).mapToPair(new PairFunction<Tuple2<String,Integer>, String, String>() {

			@Override
			public Tuple2<String, String> call(Tuple2<String, Integer> t) throws Exception {
				return new Tuple2<String, String>("upload", t._1+","+t._2);
			}
		});

		
	}
}
