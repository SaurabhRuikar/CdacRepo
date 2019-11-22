create table j_stud
(
sno number(2),
sname varchar2(15),
scont number(10),
scity varchar2(15),
sdt date
);

desc j_stud;

insert into j_stud values(1,'Uday',8888819781,'Pune','15 Oct 1981');
insert into j_stud values(2,'Rupesh',8888819781,'Pune1','15 May 1987');

insert into j_stud(scont,sno,sname) values(4523152,3,'ABC');

insert into j_stud (sno,sname,scont,scity)values(&sno,&sname,&scont,&scity);

commit;

desc user_tables;

select * from user_tables;

select * from tab;

alter table feb_b1_emp
drop column ejob;

alter table feb_b1_emp
drop column ejdt;

desc feb_b1_emp;

alter table feb_b1_emp
add ejob varchar2(10);

alter table feb_b1_emp
modify ejob varchar2(15);

alter table feb_b1_emp
rename column esal to salary;

alter table feb_b1_emp
rename to emem;

desc feb_b1_emp;

rename emem to feb_b1_emp;

select * from feb_b1_emp;

insert into feb_b1_emp values(1,'UDAY',45623,'SALESMAN');
insert into feb_b1_emp values(2,'SUNIL',45623,'CLERK');
insert into feb_b1_emp values(3,'MAHESH',null,'CLERK');

insert into feb_b1_emp(ename,salary,eno)values('MANOJ',9867,5);

insert into feb_b1_emp values(&eno,'&ename',&salary,'&ejob');


commit;

create table feb_b1_emp2 
as
select * from feb_b1_emp2;

truncate table feb_b1_emp1;

drop table feb_b1_emp2;

select * from feb_b1_emp1;

select * from ee;

select * from ee
where comm is not null;

rollback;

create table dg
( dt date
);

insert into dg values('&dt');

select sysdate from dual;

alter session
set nls_date_format = 'dd Mon yyyy';


    select * from ee;
 
update ee
set sal=sal+200,comm=comm+200
where job='SALESMAN';    

delete from ee
where job='CLERK';

rollback;


