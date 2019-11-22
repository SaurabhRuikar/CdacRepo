package org.cdac.mysparkcore;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkYoutubeAvg {

	public static void main(String[] args) {
		
		
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
				return new Tuple2<String, Integer>(words[3],Integer.parseInt(words[5]));
			}
		});
		
		JavaPairRDD<String,Iterable<Integer>> avg = wordTuple.groupByKey();
		
		avg.map(new Function<Tuple2<String,Iterable<Integer>>, String>() {

			@Override
			public String call(Tuple2<String, Iterable<Integer>> v1) throws Exception 
			{
				
				int avg = 0, count = 0, sum = 0;
				for(Integer i : v1._2)
				{
					sum += i.intValue();
					count++;
				}
				
				avg = sum/count;
				
				return v1._1+" "+avg;
			}
		}).foreach(new VoidFunction<String>() {

			@Override
			public void call(String t) throws Exception {
				// TODO Auto-generated method stub
				System.out.println(t);
				
			}
		});

	}

}
