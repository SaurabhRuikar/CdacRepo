package book;

public abstract class Book_id 
{
     protected int id;
	 private  String title;
	 private static int cnt=1;
     protected double  price;
	public Book_id() {
		super();
		// TODO Auto-generated constructor stub
	}
	public Book_id(String title, double price) {
		super();
		this.id = cnt++;
		this.title = title;
		this.price = price;
	}
     
	public abstract double calCost();
	@Override
	public String toString() 
	{
		// TODO Auto-generated method stub
		return "Id : "+id+"\nTitle : "+title+"\nPrice : "+price;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public abstract String getName();

     
}
