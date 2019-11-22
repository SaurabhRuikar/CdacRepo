package office.util;

public class Date 
{
	int dd,mm,yy;

	public Date() 
	{
		
	}

	public Date(int dd, int mm, int yy) 
	{
		this.dd = dd;
		this.mm = mm;
		this.yy = yy;
	}
	public void showDate()
	{
		System.out.println(dd+"/"+mm+"/"+yy);	
	}
	
	public void showDate(char ch)
	{
		System.out.println(dd+""+ch+mm+""+ch+yy);	
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return dd+"/"+mm+"/"+yy;
	}
	
}
