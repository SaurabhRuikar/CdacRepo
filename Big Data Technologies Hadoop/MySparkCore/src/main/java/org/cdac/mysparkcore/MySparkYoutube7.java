package org.cdac.mysparkcore;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkYoutube7 
{
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
		
		
		
		JavaPairRDD<String,Double> wordTuple = lines1.mapToPair(new PairFunction<String, String, Double>() 
		{

			@Override
			public Tuple2<String, Double> call(String t) throws Exception {
				String [] words = t.split("\t");
				return new Tuple2<String, Double>(words[3],Double.parseDouble(words[6]));
			}
		});
		
		JavaPairRDD<String,Iterable<Double>> avg = wordTuple.groupByKey();
		
		avg.map(new Function<Tuple2<String,Iterable<Double>>, String>() {

			@Override
			public String call(Tuple2<String, Iterable<Double>> v1) throws Exception 
			{
				
				Double avg = 0.0, count = 0.0, sum = 0.0;
				for(Double i : v1._2)
				{
					sum += i.doubleValue();
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
