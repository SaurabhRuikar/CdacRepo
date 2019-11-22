package org.cdac.mysparkcore;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkYoutubeTotal {

public static void main(String[] args)
	
	
	{
		JavaSparkContext context = new JavaSparkContext("local[*]", "avg");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> lines1= lines.filter(new Function<String, Boolean>() {

			@Override
			public Boolean call(String v1) throws Exception {
				// TODO Auto-generated method stub
				return v1.contains("\t") && (Integer.parseInt(v1.split("\t")[5]) > 2000);
			}
		
		});
		
		
		
		JavaPairRDD<String,Integer> wordTuple = lines1.mapToPair(new PairFunction<String, String, Integer>() 
		{

			@Override
			public Tuple2<String, Integer> call(String t) throws Exception {
				String [] words = t.split("\t");
				return new Tuple2<String, Integer>(words[3],1);
			}
		});
		
		wordTuple.reduceByKey(new Function2<Integer, Integer, Integer>() 
		{
			
			@Override
			public Integer call(Integer v1, Integer v2) throws Exception {
				// TODO Auto-generated method stub
				return v1+v2;
			}
		}).foreach(new VoidFunction<Tuple2<String,Integer>>() {
			
			@Override
			public void call(Tuple2<String, Integer> t) throws Exception {
				// TODO Auto-generated method stub
				System.out.println(t._1()+" : "+t._2());
			}
		});

		
	}


}
