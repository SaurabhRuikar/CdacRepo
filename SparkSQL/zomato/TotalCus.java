package sparksql.zomato;

import java.util.ArrayList;
import java.util.List;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Column;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.functions;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

public class TotalCus {

	public static void main(String[] args) {
		JavaSparkContext context=new JavaSparkContext("local[*]", "catcount");
		SparkSession session=SparkSession.builder().getOrCreate();
		List<StructField> fields=new ArrayList<>();
		StructField field=DataTypes.createStructField("ID", DataTypes.IntegerType, true);
		fields.add(field);
		field=DataTypes.createStructField("RestoName", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("CountryCode", DataTypes.IntegerType, true);
		fields.add(field);
		field=DataTypes.createStructField("City", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("Address", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("Locality", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("LocalityV", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("Longitude", DataTypes.DoubleType, true);
		fields.add(field);
		field=DataTypes.createStructField("Lattitude", DataTypes.DoubleType, true);
		fields.add(field);
		field=DataTypes.createStructField("Cuisines", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("AvgCost", DataTypes.IntegerType, true);
		fields.add(field);
		field=DataTypes.createStructField("Currency", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("TBook", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("OnlineD", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("IsDelivery", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("OrderMenu", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("Price", DataTypes.IntegerType, true);
		fields.add(field);
		field=DataTypes.createStructField("ArggRate", DataTypes.DoubleType, true);
		fields.add(field);
		field=DataTypes.createStructField("RatingC", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("RatingT", DataTypes.StringType, true);
		fields.add(field);
		field=DataTypes.createStructField("Votes", DataTypes.IntegerType, true);
		fields.add(field);
		
		StructType schema=DataTypes.createStructType(fields);
		Dataset<Row> you=session.read().schema(schema).option("header", true).csv(args[0]);
		you.cache();
		Dataset<Row> data=you.select(new Column("Cuisines"));
		Dataset<Row> a=data.select(functions.split(new Column("Cuisines"), ",").as("sc"));
		long res=a.select(functions.explode(new Column("sc"))).distinct().count();
		System.out.println("Count is :"+res);
		
		

	}

}
