package org.cdac.north;

import java.util.ArrayList;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

public class Assignment3 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		JavaSparkContext context = new JavaSparkContext("local[*]", "hello");
		SparkSession session = SparkSession.builder().getOrCreate();
		java.util.List<StructField> fields = new ArrayList<StructField>();
	
		StructType schema = DataTypes.createStructType(fields);
		Dataset<Row> customer = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/customers.csv");
		
		long cnt = customer.filter(new Column("Country").equalTo("Brazil")).count();
		System.out.println("Total" +cnt);
	}


}
