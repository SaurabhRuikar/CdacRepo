package org.cdac.kafka;


import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Properties;

import org.apache.kafka.clients.consumer.Consumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

public class MyTestConsumer {
	
	
	public static void main(String [] args) throws IOException {
		
		
		
		Properties properties =new Properties();
		properties.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
		properties.put(ConsumerConfig.GROUP_ID_CONFIG, "test-consumer-group");
		properties.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG,StringDeserializer.class.getName());
		properties.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
		
		java.util.List<String> topics =new ArrayList<String>();
		topics.add("test");
		
		
		
		FileWriter fw = new FileWriter("/home/student/Desktop/youtube1.json");
		KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(properties);
		consumer.subscribe(topics);
		while(true)
		{
			
			
			ConsumerRecords<String, String> crecords = consumer.poll(100000);
			for(ConsumerRecord<String, String> record : crecords)
			{
				JSONObject joObject = new JSONObject();
				String [] words = record.value().split("\t");
				if(words.length==9)
				{
					joObject.put("Id", words[0]);
					joObject.put("Uploader", words[1]);
					joObject.put("Interval", words[2]);
					joObject.put("Category", words[3]);
					joObject.put("Length", words[4]);
					joObject.put("Views", words[5]);
					joObject.put("Rating", words[6]);
					joObject.put("No_Rating", words[7]);
					joObject.put("Comments", words[8]);
				}	
				fw.append(joObject.toJSONString()+"\n");
				
			}
		}
	}

}
