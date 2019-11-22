package org.cdac.mysparkcore.zomato;



import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.api.java.function.VoidFunction;

import scala.Tuple2;

public class MySparkCoreZ8 {

	public static void main(String[] args) {
		JavaSparkContext context=new JavaSparkContext("local[*]", "catcount");
		JavaRDD<String> lines=context.textFile(args[0]);
		JavaRDD<String> words=lines.filter(new Function<String, Boolean>() {
			@Override
			public Boolean call(String v1) throws Exception {
				try {
					int data1=Integer.parseInt(v1.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)")[2]);
					return true;
				}
				catch (Exception e) {
					return false;
				}
				
			}
		});
		
		JavaPairRDD<Integer,Double> catTuple=words.mapToPair(new PairFunction<String, Integer, Double>() {

			@Override
			public Tuple2<Integer, Double> call(String t) throws Exception {
				String[]words=t.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
				int cat  = Integer.parseInt(words[16]);
				double v1=Double.parseDouble(words[17]);
				return new Tuple2<Integer, Double>(cat,v1);
			}
		});
		JavaPairRDD<Integer,Iterable<Double>> data=catTuple.groupByKey();
		
		JavaRDD<String> res=data.map(new Function<Tuple2<Integer,Iterable<Double>>, String>() {

			@Override
			public String call(Tuple2<Integer, Iterable<Double>> v1) throws Exception {
				int cnt=0;
				double sum=0;
				double avg=0;
				for(Double a:v1._2())
				{
					sum=sum+a;
					cnt++;
				}
				avg=sum/cnt;
				return v1._1()+""+avg;
			}
			
		});
		res.foreach(new VoidFunction<String>() {

			@Override
			public void call(String t) throws Exception {
				System.out.println("average is :"+t);
				
			}
			
		});
		

	}

}