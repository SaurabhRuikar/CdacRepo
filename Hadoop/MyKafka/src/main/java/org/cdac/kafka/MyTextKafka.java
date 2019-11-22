package org.cdac.kafka;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.IntegerSerializer;
import org.apache.kafka.common.serialization.StringSerializer;

public class MyTextKafka {
	public static void main(String[] args) throws IOException {
		Properties properties = new Properties();
		properties.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
		properties.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, IntegerSerializer.class);
		properties.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
		
		KafkaProducer<Integer, String> producer = new KafkaProducer<Integer, String>(properties);
		
		FileReader fr = new FileReader("/home/student/DBDA_CHEATS/Untitled Document 2");
		BufferedReader br = new BufferedReader(fr);
		
		String line = "";
		while((line=br.readLine())!=null)
		{
			
			producer.send(new ProducerRecord<Integer, String>("test", line));
			
			
		}
		producer.flush();
		
	}
}
