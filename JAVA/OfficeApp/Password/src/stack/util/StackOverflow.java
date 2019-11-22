package stack.util;

public class StackOverflow extends Exception 
{
	private String msg;

	public StackOverflow() {
		
		msg = "Stack Overflow";
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}
	
	
}
