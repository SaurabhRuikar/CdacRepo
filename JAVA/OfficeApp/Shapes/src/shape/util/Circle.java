package shape.util;

public class Circle implements Drawable 
{
	
	private double radius;
	
	

	public Circle() 
	{
		super();
		// TODO Auto-generated constructor stub
	}
	

	public Circle(double radius) 
	{
		super();
		this.radius = radius;
	}


	@Override
	public void drawShape() 
	{
		// TODO Auto-generated method stub
		System.out.println("In the drawshape methode of circle");
	}

	@Override
	public double calArea() 
	{
		// TODO Auto-generated method stub
		return pi*radius*radius;
	}

}
