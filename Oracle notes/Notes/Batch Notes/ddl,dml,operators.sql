create table emp_nishu
(
    eno number(3),
    enm varchar2(20),
    job varchar2(20),
    sal number(7,2)
   );

desc emp_nishu;
   
insert into emp_nishu values(100,'Nishant','Dev',25000);
insert into emp_nishu values(101,'Nishant1','Dev1',2500);
insert into emp_nishu(job,enm) values('Acc','UDAY');

select * from emp_nishu;

alter table emp_nishu
add dno number(3);

alter table emp_nishu
modify dno number(5);

alter table emp_nishu
drop column dno;

alter table emp_nishu
rename column sal to SALARY;

truncate table emp_nishu;

drop table emp_nishu;

rename emp_nishu to e_nishu

select * from e_nishu;

--------------------------------------------

Opertors:

--------------------------------------------

desc ee;

select * from ee;

select * from ee
where sal<2000;
