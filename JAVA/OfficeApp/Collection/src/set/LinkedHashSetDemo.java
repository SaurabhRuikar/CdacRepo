package set;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Set;

import student.Student;

public class LinkedHashSetDemo 
{
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

			Set<Student> s = new LinkedHashSet<>();
			
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
		
	}

}
