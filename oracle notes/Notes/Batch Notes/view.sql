select * from tab;

create view m_v1
as
select * from ee where deptno=10;

drop view m_v4;

select * from m_v1;

update m_v1
set gender='M'
where ename='SWARIT';

select rowid as RD, rownum from ee;

delete from m_v1
where gender='M';
rollback;


select * from m_v1;

select * from ee order by dno;


create view m_v1_v1
as
select * from m_v1 where sal>=6700;

select * from EE;

update m_v1
set sal = sal+5555;

create view m_v2
as
select e.ename,e.sal,d.dname,d.deptno from emp1 e, dept d
where e.deptno=d.deptno;

select * from m_v2;

insert into m_v2 values('DDD',5000,'SALES',30)

drop view m_v3;


create view m_v3
as 
select * from ee
with read only;

select * from m_v3;

update m_v3
set sal = sal+5555;

create view m_v4
as
select * from m_v3;

select * from m_v3_v3;

update m_v3_v3
set sal = sal+5555;


create force view m_vv4
as
select * from dk;

DROP TABLE dk;

select * from m_vv4;

select rowid as rd, rownum from ee;


create table dk
(
no number,
nm varchar2(10)
);



insert into dk values(1,'A');
insert into dk values(2,'B');
insert into dk values(3,'C');
insert into dk values(4,'D');
insert into dk values(5,'E');
