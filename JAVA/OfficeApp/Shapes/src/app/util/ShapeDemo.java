package app.util;

import shape.util.Circle;
import shape.util.Drawable;
import shape.util.Rectangle;

public class ShapeDemo 
{

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Drawable [] d = {new Rectangle(10, 12),
						 new Circle(7)};
		System.out.println("-----------------------------------");
		for(int i = 0; i < d.length ; i++)
		{
			d[i].drawShape();
			System.out.println("Area is : "+d[i].calArea());
			System.out.println("-----------------------------------");
		}
		
		//System.out.println("With advanced for loop");
		
		for(Drawable dr : d)
		{
			dr.drawShape();
			System.out.println("Area is : "+dr.calArea());
			System.out.println("-----------------------------------");
		}

	}
}
