package app;

public class NumberException extends Exception{

	
	private String str ="number is incorrect";

	public NumberException() {
	
	}

	@Override
	public String getMessage() {
		// TODO Auto-generated method stub
		return str;
	}
	
}
