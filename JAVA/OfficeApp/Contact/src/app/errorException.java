package app;

public class errorException extends Exception {

	
	
	private String str ="name is incorrect";

	public errorException(String str) {
		super();
		this.str = str;
	}

	@Override
	public String getMessage() {
		// TODO Auto-generated method stub
		return str;
	}
	
	
	
	
}
