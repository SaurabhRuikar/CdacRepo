package mongodb;

import java.util.Collection;
import java.util.Set;

import com.mongodb.BasicDBObject;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.MongoClient;

public class InsertMongo {

	public static void main(String[] args) {
		
		
		MongoClient mongo =new MongoClient();
		DB database = mongo.getDB("mydb");
		DBCollection collection=database.getCollection("emp");
		
		System.out.println("Connected with server");
		System.out.println("=====================");
		
		//insertion
		
		BasicDBObject document =new BasicDBObject();
		document.put("name", "saurabh");
		collection.insert(document);
		System.out.println("inserted");

		//deleting
		
		collection.remove(document);
		System.out.println("deleted");

		//finding with condition

		BasicDBObject q1 = new BasicDBObject();
		q1.put("sal", new BasicDBObject("$gte",10000));
		DBCursor cs = collection.find(q1);
		while(cs.hasNext())
		{
			System.out.println(cs.next());
		}
		
		//update
		
		BasicDBObject q2 = new BasicDBObject();
		q2.put("ename","saurabh");
		
		BasicDBObject q4 = new BasicDBObject();
		q4.put("ename", "prashant");
		
		BasicDBObject q3 = new BasicDBObject();
		q3.put("$set", q4);
		
		collection.update(q2, q3);
		System.out.println("updated");
		
       
        		
		
		
		
		
	}

}
