package org.cdac.testsparkstream;

import java.sql.Array;
import java.util.Arrays;
import java.util.Iterator;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.function.FlatMapFunction;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.streaming.Duration;
import org.apache.spark.streaming.api.java.JavaReceiverInputDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;

import scala.Tuple2;

public class TestSparkStream {

	public static void main(String[] args) throws InterruptedException {
		
		SparkConf conf = new SparkConf();
		conf.setMaster("local[*]");
		
		JavaStreamingContext context = new JavaStreamingContext(conf, new Duration(5000));
		JavaReceiverInputDStream<String> lines = context.socketTextStream("localhost", 9991);
		
		lines.flatMap(new FlatMapFunction<String, String>() {

			public Iterator<String> call(String t) throws Exception {
				// TODO Auto-generated method stub
				return Arrays.asList(t.split(" ")).iterator();
			}
		}).mapToPair(new PairFunction<String, String, Integer>() {

			public Tuple2<String, Integer> call(String t) throws Exception {
				// TODO Auto-generated method stub
				return new Tuple2<String, Integer>(t, 1);
			}
		}).reduceByKey(new Function2<Integer, Integer, Integer>() {
			
			public Integer call(Integer v1, Integer v2) throws Exception {
				// TODO Auto-generated method stub
				return v1+v2;
			}
		}).print();
		
		
		context.start();
		context.awaitTermination();
	}

}
