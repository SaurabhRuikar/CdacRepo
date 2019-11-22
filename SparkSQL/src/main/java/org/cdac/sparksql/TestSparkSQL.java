package org.cdac.sparksql;

import java.util.ArrayList;

import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

public class TestSparkSQL {

	public static void main(String[] args) 
	{
		
		SparkSession session = SparkSession.builder().getOrCreate();
		java.util.List<StructField> fields = new ArrayList<StructField>();
		
		fields.add(DataTypes.createStructField("Name", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Department", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Manager", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Gender", DataTypes.StringType, true));
		fields.add(DataTypes.createStructField("Salary", DataTypes.IntegerType, true));
		fields.add(DataTypes.createStructField("Age", DataTypes.IntegerType, true));
		
		StructType schema = DataTypes.createStructType(fields);
		
		session.read().schema(schema).option("header", true).csv(args[0]).show();

	}

}
