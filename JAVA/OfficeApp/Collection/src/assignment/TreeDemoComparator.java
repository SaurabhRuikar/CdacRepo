import java.util.Comparator;
import java.util.Set;
import java.util.TreeSet;

import student.Student;

public class TreeDemoComparator {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

			Set<Student> s = new TreeSet<>(new Comparator<Student>() {

				@Override
				public int compare(Student o1, Student o2) {
					// TODO Auto-generated method stub
					return o1.getId() - o2.getId();
				}
			});
			 
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
	}}
