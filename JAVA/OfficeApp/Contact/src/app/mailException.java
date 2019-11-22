package app;

public class mailException extends Exception{
	
	private String str1 = "Invalid e_mail Id";

	public mailException() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	public String getMessage1() {
		// TODO Auto-generated method stub
		return str1;
	}

}
