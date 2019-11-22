package assignment;

public class Cocacola {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		String str = "cocabola";
		int c=0,o=0,a=0,l=0;
		for(int i=0;i<str.length();i++)
		{
			if(str.charAt(i)=='c')
				c++;
			if(str.charAt(i)=='o')
				o++;
			if(str.charAt(i)=='a')
				a++;
			if(str.charAt(i)=='l')
				l++;
		}
		System.out.println("c : "+c+"\no : "+o+"\na : "+a+"\nl : "+l);
	}

}
