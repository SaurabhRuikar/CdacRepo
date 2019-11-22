package student;

public class Student implements Comparable<Student>
{
	private int id;
	private String name;
	private double marks;
	public Student() {
		super();
		// TODO Auto-generated constructor stub
	}
	public Student(int id, String name, double marks) {
		super();
		this.id = id;
		this.name = name;
		this.marks = marks;
	}
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public double getMarks() {
		return marks;
	}
	public void setMarks(double marks) {
		this.marks = marks;
	}
	@Override
	public int hashCode() 
	{
		int code=0;
		String str = this.name.toUpperCase();
		for(int i = 0;i<str.length();i++)
			code+=str.charAt(i);
		return code;
	}
	
	@Override
	public boolean equals(Object obj) 
	{
		if(obj instanceof Student)
		{
			Student s = (Student)obj;
			if(this.id==s.id && this.name.equals(s.name) && this.marks==s.marks)
				return true;
			else
				return false;
		}
		else
			return false;
	}
	@Override
	public String toString() {
		// TODO Auto-generated method stub
		return "Id : "+id+"\nName : "+name+"\nMarks : "+marks;
	}
	@Override
	public int compareTo(Student o) 
	{
		// TODO Auto-generated method stub
		return o.id - this.id;
	}
	
	
}
