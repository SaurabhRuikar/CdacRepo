package stack.util;

public class Password_validation extends Exception
{

	String msg;

	public Password_validation() {
		
	msg = "Password shoud have special character";
	

	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "pass is not valid";
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}
 
	
	
	
	
	

}
