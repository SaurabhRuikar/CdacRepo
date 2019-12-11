SELECT * FROM STUD_MAR;

truncate table stud_mar 

insert into stud_mar values(1,'Uday','23 Oct 1980','M');
insert into stud_mar values(2,'Ravi','15 Apr 1992','M');
insert into stud_mar values(3,'Pravin','5 Mar 1999','M');

commit;
rollback;

insert into stud_mar values(4,'Yogesh','20 Oct 2012','M');
insert into stud_mar values(5,'Pravin','5 Mar 1999','M');
insert into stud_mar values(6,'Yogesh','20 Oct 2012','M');
insert into stud_mar values(7,'Yogeshwari','10 Oct 2013','F');

SAVEPOINT n1;

update stud_mar
set sname = 'Yogita', gen = 'F'
where sno=4;

SAVEPOINT n2;

select * from stud_mar;

delete from stud_mar
where sno<2;

SAVEPOINT n3;

rollback to n1;

select * from stud_mar;
select * from ee;

rollback to n1;

-- Locking Concepts:

update stud_mar
set sname = 'Pratiksha' where sno=3;

select * from stud_mar;

update stud_mar
set GEN = 'M'
where sno=4;

commit;



