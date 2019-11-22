package util;

import java.io.Serializable;

public class Contact implements Serializable
{

	private String name,email_id;
	private String mobile;
	public Contact() {
		super();
		// TODO Auto-generated constructor stub
	}
	public Contact(String name, String email_id, String mobile) {
		super();
		this.name = name;
		this.email_id = email_id;
		this.mobile = mobile;
		
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Name : "+name+"\nEmail Id : "+email_id+"\nMobile : "+mobile;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getEmail_id() {
		return email_id;
	}
	public void setEmail_id(String email_id) {
		this.email_id = email_id;
	}
	public String getMobile() {
		return mobile;
	}
	public void setMobile(String mobile) {
		this.mobile = mobile;
	}	
	
	
	
}
