package org.cdac.mysparkcore.zomato;

import java.util.Arrays;
import java.util.Iterator;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkCoreZ3 {
	
	
	public static <U> void main(String[] args) {
		
		JavaSparkContext context = new JavaSparkContext("local[*]", "avg");
		JavaRDD<String> lines = context.textFile(args[0]);
		JavaRDD<String> lines1=lines.filter(new Function<String, Boolean>() {
			
			public Boolean call(String v1) throws Exception {
				// TODO Auto-generated method stub
				try
				{
					String data= (v1.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)")[3]);
					return true;
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
				return new Tuple2<String, Integer>(words[9], 1);
			}
		});
		
		JavaRDD<String> flatWord = wordTuple.flatMap(new FlatMapFunction<Tuple2<String,Integer>, String>() {

			@Override
			public Iterator<String> call(Tuple2<String, Integer> t) throws Exception {
				String [] words = t._1.split(",");
				return Arrays.asList(words).iterator();
			}
		});
		
		JavaPairRDD<String,Integer> data= flatWord.mapToPair(new PairFunction<String, String, Integer>() {

			@Override
			public Tuple2<String, Integer> call(String t) throws Exception {
				// TODO Auto-generated method stub
				return new Tuple2<String, Integer>(t, 1);
			}
		});
		JavaPairRDD<String, Integer> data1 = data.reduceByKey(new Function2<Integer, Integer, Integer>() {

			public Integer call(Integer v1, Integer v2) throws Exception {
				// TODO Auto-generated method stub
				return v1+v2;
			}
		});
		System.out.println("Cuisines : "+data1.count());
		

	}

}
