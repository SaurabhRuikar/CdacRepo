package org.cdac.mysparkcore;

import java.util.Arrays;
import java.util.Iterator;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class TestSparkCore {

	public static void main(String[] args) {
		
		
		// TODO Auto-generated method stub

		JavaSparkContext context = new JavaSparkContext("local[*]", "worlCOunt");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> word = lines.flatMap(new FlatMapFunction<String, String>() 
		{
			public Iterator<String> call(String t) throws Exception 
			{
				String words[] = t.split(",");
				
				return Arrays.asList(words).iterator();
			}				
		});
		
		JavaPairRDD<String, Integer> wordtuple=word.mapToPair(new PairFunction<String, String, Integer>()
		{

			public Tuple2<String, Integer> call(String t) throws Exception {
				// TODO Auto-generated method stub
				return new Tuple2<String, Integer>(t, 1);
			}
		});
		
		JavaPairRDD<String, Integer> wordCount = wordtuple.reduceByKey(new Function2<Integer, Integer, Integer>() 
		{
			
			public Integer call(Integer v1, Integer v2) throws Exception {
				// TODO Auto-generated method stub
				return v1+v2;
			}
		});
		
		wordCount.foreach(new VoidFunction<Tuple2<String,Integer>>() 
		{
			
			public void call(Tuple2<String, Integer> t) throws Exception {
				// TODO Auto-generated method stub
				System.out.println(t._1+" : "+t._2);
			}
		});
		
	}

}
