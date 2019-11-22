package org.cdac.mysparkcore.zomato;

import java.util.Arrays;
import java.util.Iterator;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkCoreZ4 {
	
	
	
	public static <U> void main(String[] args) {
		
		JavaSparkContext context = new JavaSparkContext("local[*]", "avg");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> lines1=lines.filter(new Function<String, Boolean>() {
			
			public Boolean call(String v1) throws Exception {
				// TODO Auto-generated method stub
				try
				{
					String []data= (v1.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)"));
					String data1 = (v1.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)")[3]);
					return data[12].contains("Yes");
				}
				catch(Exception e)
				{
					return false;
				}
				
				
			}
		});
		
		JavaPairRDD<String,Integer> wordTuple = lines1.mapToPair(new PairFunction<String, String, Integer>() {

			public Tuple2<String, Integer> call(String t) throws Exception {
				String [] words = t.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
				return new Tuple2<String, Integer>(words[1], 1);
			}
		});
		
		
		
		JavaPairRDD<String, Integer> data1 = wordTuple.reduceByKey(new Function2<Integer, Integer, Integer>() {

			public Integer call(Integer v1, Integer v2) throws Exception
			{
				// TODO Auto-generated method stub
				return null;
			}
		});
		data1.foreach(new VoidFunction<Tuple2<String,Integer>>() {

			@Override
			public void call(Tuple2<String, Integer> t) throws Exception {
				// TODO Auto-generated method stub
				System.out.println(t._1);
				
			}
		});
		
		

	}
	

}
