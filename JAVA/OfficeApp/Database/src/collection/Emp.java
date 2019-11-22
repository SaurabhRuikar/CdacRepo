package collection;

public class Emp 
{
	private int emp_id,sal;
	private String ename;
	
	
	public Emp(int emp_id, String ename, int sal) {
		super();
		this.emp_id = emp_id;
		this.sal = sal;
		this.ename = ename;
	}


	public int getEmp_id() {
		return emp_id;
	}


	public void setEmp_id(int emp_id) {
		this.emp_id = emp_id;
	}


	public int getSal() {
		return sal;
	}


	public void setSal(int sal) {
		this.sal = sal;
	}


	public String getEname() {
		return ename;
	}


	public void setEname(String ename) {
		this.ename = ename;
	}


	@Override
	public String toString() {
		return "Emp [emp_id=" + emp_id + ", sal=" + sal + ", ename=" + ename + "]";
	}	
	
	
	
}
