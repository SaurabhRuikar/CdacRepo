package mongodb;

import java.util.Set;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.MongoClient;

public class MongoFind {

	public static void main(String[] args) {
		
		MongoClient mongo =new MongoClient();
		DB database = mongo.getDB("mydb");
		System.out.println("Connected with server");
		DBCollection collection=database.getCollection("emp");
		BasicDBObject query=new BasicDBObject();
		
		DBCursor cursor= collection.find();
		while(cursor.hasNext())
		{
			
			System.out.println(cursor.next());
			
			
			
		}
		

	}
}
