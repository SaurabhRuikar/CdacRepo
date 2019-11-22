package book;

public class Ebook extends Book_id {
	
	
	private double discount=50;

	public Ebook() {
		// TODO Auto-generated constructor stub
	}

	public Ebook(String title, double price) 
	{
		super(title, price);
		
		// TODO Auto-generated constructor stub
	}

	@Override
	public double calCost() {
		// TODO Auto-generated method stub
		return (super.price-discount);
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString();
	}
	
	public String getName()
	{
		return "ebook";
	}
	

}
