package book;

public class IdNotfoundException extends Exception 
{

	private String msg="Book Id Not Found";
	
	public IdNotfoundException() {
		super();
		// TODO Auto-generated constructor stub
	}
	@Override
	public String getMessage() {
		// TODO Auto-generated method stub
		return msg;
	}
	
		
}
