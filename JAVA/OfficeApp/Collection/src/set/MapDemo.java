package set;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo {

	public static void main(String[] args) 
	{
		
		Map<Integer, String> map=new LinkedHashMap<>();
		
		map.put(10, "ten");
		map.put(11, "eleven");
		map.put(12, "twelve");
		map.put(13, "thirteen");
		map.put(10, "ten");
		map.put(11, "eleven");
		map.put(9, "nine");
		map.put(9, "nineeee");
     
		Set<Map.Entry<Integer, String>> s=map.entrySet();
		
		for(Map.Entry<Integer, String> m:s)
		{
			System.out.println(m.getKey()+" : "+m.getValue());		
		}
	}

}
