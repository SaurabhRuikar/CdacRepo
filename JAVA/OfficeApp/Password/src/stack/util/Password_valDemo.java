package stack.util;

public class Password_valDemo {

	public static void main(String[] args){
		// TODO Auto-generated method stub

		try
		{
		int l = args[0].length(),cnts=0,cntn=0;
		String a = args[0];
		if(l>5 && l<10)
		{
		
			for(int i=0;i<l;i++)
			{
				if(a.charAt(i)>=33 && a.charAt(i)<=47)
				{
					cnts++;				
				}
				if(a.charAt(i)>=47 && a.charAt(i)<=57)
				{
					cntn++;				
				}
			}
		}
		if(cnts>0 && cntn>0)
			System.out.println("Password Is Valid");
		else
			throw new Password_validation();
		}
		catch(Password_validation e)
		{
			System.out.println(e.getMsg());
			e.printStackTrace();
			
		}
	}

}
