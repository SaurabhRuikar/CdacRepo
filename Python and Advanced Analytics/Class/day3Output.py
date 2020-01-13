Python 3.5.2 (default, Oct  8 2019, 13:06:37) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter the number6
Not a Prime
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter the number7
Prime
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
20 10 7 5 1 
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1 5 7 10 20 
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
20 10 7 5 1 
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
[5, 7, 10, 20, 1]
20 10 7 5 1 
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
[5, 7, 10, 20, 1]
20 10 7 5 1 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
[5, 7, 10, 20, 1]
20 10 7 5 1 1
2
3
4
5
6
7
8
9
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
[5, 7, 10, 20, 1]
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 32, in <module>
    for i in reversed(lst,reverse=True):
TypeError: reversed() does not take keyword arguments
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
[5, 7, 10, 20, 1]
1 20 10 7 5 
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 a 40
20 b 50
30 c 60
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 a 40
20 b 50
30 c 60
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 40 a
20 50 b
30 60 c
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 10 10
20 20 20
30 30 30
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 a 40
20 b 50
30 c 60
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
0 10
1 20
2 30
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
0 10
1 20
2 30
11 10
12 20
13 30
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 72, in <module>
    for i,j,k in enumerate(zip(lst,lst1),11):
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 73, in <module>
    print(i,j,k)
NameError: name 'k' is not defined
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 a
20 b
30 c
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 72, in <module>
    for i,j in enumerate(lst,lst1):
TypeError: 'list' object cannot be interpreted as an integer
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10 a
20 b
30 c
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
0 (10, 'a')
1 (20, 'b')
2 (30, 'c')
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
11 (10, 'a')
12 (20, 'b')
13 (30, 'c')
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
11 (10, 'a') [2]
12 (20, 'b') [2]
13 (30, 'c') [2]
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 73, in <module>
    print(i[0],i[1],i[2])
IndexError: tuple index out of range
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
11 (10, 'a')
12 (20, 'b')
13 (30, 'c')
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 72, in <module>
    for i,j,k in zip(enumerate(lst,11),lst1):
ValueError: not enough values to unpack (expected 3, got 2)
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
(11, 10) a
(12, 20) b
(13, 30) c
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 73, in <module>
    print(i[0],i[1],i[2])
IndexError: tuple index out of range
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
11 10 a
12 20 b
13 30 c
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
10
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number10
Not found
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number10
Index is 0
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number50
Not found
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number40
Index is 3
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number10
Index is 1
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number10
Index is 0
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter the number50
Not found
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 128, in <module>
    s25=s12.minus(s11)
AttributeError: 'set' object has no attribute 'minus'
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
Subset
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
Subset
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 10, 20, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 45, 20, 23, 30}
{40, 10, 20, 30}
{45, 23}
Subset
True
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 152, in <module>
    print(s.remove(40))
KeyError: 40
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
None
{10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
None
{10, 20, 30}
None
{10, 20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
None
{10, 20, 30}
None
{20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
{40, 50, 10, 20, 30}
40
{50, 10, 20, 30}
None
{10, 20, 30}
None
{20, 30}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
enter treemango
Continuey
enter treeMango
Continuen
{'Mango', 'mango'}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
frozenset({40, 50, 10, 20, 30})
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
frozenset({40, 50, 10, 20, 30})
Traceback (most recent call last):
  File "/home/student/Desktop/Python/Class/Day3.py", line 180, in <module>
    fs.add(50)
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER10
Continue y/n?y
Enter a NUMBER20
Continue y/n?y
Enter a NUMBER30
Continue y/n?n
{'10', '30', '20'}
Enter a NUMBER30
Continue y/n?y
Enter a NUMBER30
Continue y/n?y
Enter a NUMBER30
Continue y/n?y
Enter a NUMBER20
Continue y/n?y
Enter a NUMBER60
Continue y/n?n
{'60', '20', '30'}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER (Set 1)10
Continue y/n?1y
Enter a NUMBER (Set 1)50
Continue y/n?y
Enter a NUMBER (Set 1)66
Continue y/n?y30
Enter a NUMBER (Set 2)30
Continue y/n?y
Enter a NUMBER (Set 2)
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER (Set 1)30
Continue y/n?y
Enter a NUMBER (Set 1)20
Continue y/n?y
Enter a NUMBER (Set 1)35
Continue y/n?y
Enter a NUMBER (Set 1)10
Continue y/n?n
Enter a NUMBER (Set 2)22
Continue y/n?y
Enter a NUMBER (Set 2)22
Continue y/n?y
Enter a NUMBER (Set 2)20
Continue y/n?y
Enter a NUMBER (Set 2)10
Continue y/n?n
Set 1 is 
{'30', '10', '35', '20'}
Set 2 is 
{'10', '22', '20'}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER (Set 1)20
Continue y/n?y
Enter a NUMBER (Set 1)10
Continue y/n?y
Enter a NUMBER (Set 1)30
Continue y/n?n
Enter a NUMBER (Set 2)34
Continue y/n?y
Enter a NUMBER (Set 2)30
Continue y/n?y
Enter a NUMBER (Set 2)20
Continue y/n?y
Enter a NUMBER (Set 2)10
Continue y/n?y
Enter a NUMBER (Set 2)40
Continue y/n?n
Set 1 is 
{'20', '30', '10'}
Set 2 is 
{'20', '34', '10', '40', '30'}
Union is:
{'10', '40', '20', '34', '30'}
Intersection is:
{'20', '10', '30'}
Difference is:
set()
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER (Set 1)10
Continue y/n?y
Enter a NUMBER (Set 1)20
Continue y/n?y
Enter a NUMBER (Set 1)30
Continue y/n?n
Enter a NUMBER (Set 2)22
Continue y/n?y
Enter a NUMBER (Set 2)10
Continue y/n?y
Enter a NUMBER (Set 2)20
Continue y/n?y
Enter a NUMBER (Set 2)22
Continue y/n?y
Enter a NUMBER (Set 2)30
Continue y/n?n
Set 1 is 
{'30', '10', '20'}
Set 2 is 
{'30', '10', '22', '20'}
Union is:
{'22', '30', '10', '20'}
Intersection is:
{'30', '10', '20'}
Difference is:
set()
None
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter a NUMBER (Set 1)10
Continue y/n?y
Enter a NUMBER (Set 1)20
Continue y/n?y
Enter a NUMBER (Set 1)30
Continue y/n?n
Enter a NUMBER (Set 2)22
Continue y/n?y
Enter a NUMBER (Set 2)10
Continue y/n?y
Enter a NUMBER (Set 2)20
Continue y/n?y
Enter a NUMBER (Set 2)67
Continue y/n?n
Set 1 is 
{'10', '20', '30'}
Set 2 is 
{'10', '22', '67', '20'}
Union is:
{'22', '67', '30', '10', '20'}
Intersection is:
{'10', '20'}
Difference is:
{'30'}
{'22', '67', '30', '10', '20'}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namedac
Not found
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namedac
Found 97
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namedbda
Found 51
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namevlsi
Found -1
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namevlsi
Not found
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namedac
Found 97
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course namevlsi
Not found
{'dbda': 51, 'dtiss': 78, 'dac': 97, 'VLSI': 1000}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course nameVLSI
Not found
{'VLSI': 1000, 'dbda': 51, 'dac': 97, 'dtiss': 78}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
Enter course nameVLSI
Found 1000
78
{'VLSI': 1000, 'dac': 97, 'dbda': 51}
>>> 
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice1
Enter the course you want to add?vlsi
Enter Value for the above Course10
Do you want to continue? y/nn
{'vlsi': '10'}
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice1
Enter the course you want to add?vlsi
Enter Value for the above Course10
Do you want to continue? y/ny
{'vlsi': '10'}
Enter the course you want to add?dac
Enter Value for the above Course1
Do you want to continue? y/ny
{'vlsi': '10', 'dac': '1'}
Enter the course you want to add?dbda
Enter Value for the above Course7
Do you want to continue? y/ny
{'vlsi': '10', 'dac': '1', 'dbda': '7'}
Enter the course you want to add?dbsa
Enter Value for the above Course8
Do you want to continue? y/ny
{'dbsa': '8', 'vlsi': '10', 'dac': '1', 'dbda': '7'}
Enter the course you want to add?dbda
Enter Value for the above Course9
Do you want to overwrite? y/nn
Overwritten
Do you want to continue? y/nn
{'dbsa': '8', 'vlsi': '10', 'dac': '1', 'dbda': '9'}
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice2
Enter the course you want to delete?vlsi
Do you want to continue? y/ny
{'dbsa': '8', 'dac': '1', 'dbda': '9'}
Enter the course you want to delete?vlsi
Already Deleted. Please Try another value
Do you want to continue? y/nn
{'dbsa': '8', 'dac': '1', 'dbda': '9'}
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice1
Enter the course you want to add?dbda
Enter Value for the above Course10
Do you want to continue? y/ny
{'dbda': '10'}
Enter the course you want to add?dac
Enter Value for the above Course20
Do you want to continue? y/ny
{'dbda': '10', 'dac': '20'}
Enter the course you want to add?vlsi
Enter Value for the above Course30
Do you want to continue? y/ny
{'dbda': '10', 'vlsi': '30', 'dac': '20'}
Enter the course you want to add?dbda
Enter Value for the above Course200
Do you want to overwrite? y/ny
Overwritten
Do you want to continue? y/nn
{'dbda': '200', 'vlsi': '30', 'dac': '20'}
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice2
Enter the course you want to delete?dbda
Do you want to continue? y/ny
{'vlsi': '30', 'dac': '20'}
Enter the course you want to delete?dbda
Already Deleted. Please Try another value
Do you want to continue? y/nn
{'vlsi': '30', 'dac': '20'}
1. add course
2. delete course
3. update course
4. remove course
5. find course
6 find course
7. display all
enter choice
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1. add course
2. delete course
3. update number
4. remove course
5. find course
6 find value
7. display all
enter choice
============ RESTART: /home/student/Desktop/Python/Class/Day3.py ============
1. add course
2. delete course
3. update number
4. remove course
5. find course
6 find value
7. display all
enter choice1
Enter the course you want to add?
