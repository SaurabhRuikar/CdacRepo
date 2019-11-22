package org.cdac.sparksql;

import java.util.ArrayList;

import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

public class YoutubeSql3 
{
	
	public static void main(String[] args) 
	{
		
		SparkSession session = SparkSession.builder().getOrCreate();
		java.util.List<StructField> fields = new ArrayList<StructField>();
		
		fields.add(DataTypes.createStructField("Id", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Uploader", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Interval", DataTypes.IntegerType, true));
		fields.add(DataTypes.createStructField("Category", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("length", DataTypes.IntegerType, true));
		fields.add(DataTypes.createStructField("Views", DataTypes.IntegerType, true));
		fields.add(DataTypes.createStructField("Rating", DataTypes.DoubleType, true));
		fields.add(DataTypes.createStructField("Ratings", DataTypes.IntegerType, true));
		fields.add(DataTypes.createStructField("Comments", DataTypes.IntegerType, true));
		
		StructType schema = DataTypes.createStructType(fields);
		
		Dataset<Row> youtube = session.read().schema(schema).csv(args[0]);
		
		youtube.cache();
		
		youtube.groupBy(new Column("Category")).avg("Views").show(); //3

		

	}

}
