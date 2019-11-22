package app;

import office.util.Date;

public class DateDemo 
{
	public static void main(String[] args) 
	{
		Date d1 = new Date();
		d1.showDate();
		Date d2 = new Date(17, 12, 1998);
		d2.showDate('-');
	}
}
