package stack.util;

public class StackUnderflow extends Exception 
{
	private String msg;

	public StackUnderflow() {
		
		msg = "Stack Underflow";
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return msg;
	}
	
	
}
