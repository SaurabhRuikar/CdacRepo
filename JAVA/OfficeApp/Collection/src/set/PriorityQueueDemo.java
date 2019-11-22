package set;
import java.util.*;
import student.Student;

public class PriorityQueueDemo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		PriorityQueue<Student> s=new PriorityQueue<>();
		s.add(new Student(1, "Vishal", 80));
		s.add(new Student(2, "Kiran", 78));
		s.add(new Student(1, "Vishal", 80));
		s.add(new Student(1, "Vishal", 80));
		s.add(new Student(3, "Ankit", 81));
		s.add(new Student(4, "Kunal", 80));
		
		for(Student s1 : s)
		{
			System.out.println(s1);
			System.out.println("==========================");				
		}
		System.out.println("first element :"+s.peek());
		System.out.println("Size is : "+s.size());
		System.out.println("popped element :"+s.poll());
		System.out.println("Size is : "+s.size());
	}

}
