package book;

public class Paper_book extends Book_id
{
  
	private double d_charges=50;
	
	public Paper_book() {
		// TODO Auto-generated constructor stub
	}

	

	public Paper_book(String title, double price) {
		super(title, price);
	}



	@Override
	public double calCost() {
		// TODO Auto-generated method stub
		return super.price+d_charges;
	}



	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return super.toString();
	}
	
	public String getName()
	{
		return "paper";
	}

}
