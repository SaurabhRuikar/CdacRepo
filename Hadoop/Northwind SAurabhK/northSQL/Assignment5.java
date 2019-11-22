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

public class Assignment5 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		JavaSparkContext context = new JavaSparkContext("local[*]", "hello");
		SparkSession session = SparkSession.builder().getOrCreate();
		java.util.List<StructField> fields = new ArrayList<StructField>();
	
		StructType schema = DataTypes.createStructType(fields);
		
		Dataset<Row> orderdetails = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/order-details.csv");
		Dataset<Row> customer = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/customers.csv");
		Dataset<Row> order = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/orders.csv");
		Dataset<Row> product = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/products.csv");
		Dataset<Row> categories = session.read().option("delimiter", "|").option("header", true).csv("/home/student/DBDA_CHEATS/Hadoop/import-northwind-master/categories.csv").filter(new Column("Description").equalTo("Cheeses")).select("CategoryID");
		categories.show();
		
		Dataset<Row> join1 = order.join(customer, customer.col("CustomerID").equalTo(order.col("CustomerID")));
		join1.show();
		Dataset<Row> join2 = orderdetails.join(join1, join1.col("OrderID").equalTo(orderdetails.col("OrderID")));
	
		Dataset<Row> join3 = product.join(join2, join2.col("ProductID").equalTo(product.col("ProductID")));
		
		long cnt = categories.join(join3, join3.col("CategoryID").equalTo(categories.col("CategoryID"))).count();
		System.out.println("Count is "+cnt);
	}
}
