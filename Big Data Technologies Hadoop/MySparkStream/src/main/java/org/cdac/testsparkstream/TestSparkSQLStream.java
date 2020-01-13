package org.cdac.testsparkstream;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.streaming.OutputMode;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.StreamingQueryException;

public class TestSparkSQLStream {
	
	
public static void main(String[] args) throws StreamingQueryException  {
	
	SparkSession session =SparkSession.builder().getOrCreate();
	Dataset<Row> data=session.readStream().format("socket").option("host", "localhost").option("port", 9991).load();
	
	
	StreamingQuery query = data.writeStream().outputMode(OutputMode.Append()).format("console").start();
	
	query.awaitTermination();
		
	}

}
