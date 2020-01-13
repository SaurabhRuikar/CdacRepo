-- Sequence

Sequence Generator:

-Db object.
-serial numbers-generates

Two Psuedo Columns generated automatically when you creates SG:
1) CURRVAL
2) NEXTVAL

Advantages:
----------------------
Generating the PK value automatically
All this serial numbers are fetch from RAM so fast access
One SG can uses in any number of tables - reusable.

select * from user_sequences;


Syntax:
drop sequence sg1;

create sequence sg1
start with 5
increment by 5
maxvalue 20
cycle
cache 3

create sequence sg3
start with 10
increment by 5
maxvalue 100
cycle
cache 10;

alter sequence sg2
maxvalue 100;

create sequence sg1; 

alter sequence sg1
nocycle;

drop table ssg2;

select sg1.currval from dual;

select * from user_sequences;

drop table ssg;

create table ssg
(
id number,
name varchar2(15)
);

create table m_2
(
id number primary key,
name varchar2(15)
);

drop table m_2;

select * from ssg;

select * from m_2;

SELECT SG1.CURRVAL FROM DUAL;


insert into ssg values(sg1.nextval,'ABC');
insert into SSG values(sg1.currval,'UDAY');
insert into ssg values(sg1.nextval,'UDAY1');
insert into ssg values(sg1.nextval,'UDAY2');
insert into ssg values(sg1.nextval,'UDAY3');
insert into ssg values(sg1.nextval,'UDAY4');
insert into ssg values(sg1.nextval,'UDAY5');
insert into ssg values(sg1.currval,'UDAY6');
select * from ssg;

select sg1.currval from dual;

select sg1.currval from dual;

alter sequence sg1
nocycle;

alter sequence sg1
maxvalue 100;

select sg1.currval from dual;


insert into m_2 values(sg1.currval,'ABC');
insert into m_2 values(sg1.nextval,'UDAY');
insert into m_2 values(sg1.nextval,'UDAY1');
insert into m_2 values(sg1.nextval,'UDAY2');
insert into m_2 values(sg1.nextval,'UDAY3');

explain plan for
select * from ssg
where id=5;

select * from table(dbms_xplan.display());

select sg1.currval, sg2.currval from dual;

insert into ssg values(sg2.nextval,'UDAY2');
insert into ssg values(sg2.nextval,'UDAY3');
insert into ssg values(sg2.nextval,'UDAY4');
insert into ssg values(sg2.nextval,'UDAY5');
insert into ssg values(sg1.currval,'UDAY6');


select * from ssg;

delete from ssg
where id = 51;

alter table ssg
add constraint ssk primary key(id);

create table sg2
(
id number primary key,
name varchar2(15)
);

drop table ssg22;
select * from ssg22;
insert into ssg22 values(sg2.nextval,'UDAY1');
insert into ssg22 values(sg2.nextval,'UDAY2');
insert into ssg22 values(sg2.nextval,'UDAY3');
insert into ssg22 values(sg2.nextval,'UDAY4');
insert into ssg22 values(sg2.nextval,'UDAY5');

select * from ssg22;

alter sequence ssg1
maxvalue 161
cycle
cache 10;

alter sequence ssg2
increment by 1
maxvalue 10
no cycle
cache 5;

create sequence ssg3
start with 5
increment by 1
maxvalue 10
cache 5

insert into ssg22 values(ssg3.nextval,'UDAY');
insert into ssg22 values(ssg3.nextval,'UDAY1');
insert into ssg22 values(ssg3.nextval,'UDAY2');
insert into ssg22 values(ssg3.nextval,'UDAY3');
insert into ssg22 values(ssg3.nextval,'UDAY4');
insert into ssg22 values(ssg3.nextval,'UDAY5');
insert into ssg22 values(ssg3.currval,'UDAY6');

select * from ssg22;

delete from ssg22;

create table ssg2
(
name varchar2(15)
);

insert into ssg2 values('UDAY');
insert into ssg2 values('UDAY1');
insert into ssg2 values('UDAY2');
insert into ssg2 values('UDAY3');
insert into ssg2 values('UDAY4');
insert into ssg2 values('UDAY5');
insert into ssg2 values('UDAY6');

alter table ssg2
add id number;


update ssg2
set id=ssg1.nextval

select * from ssg2;

commit;

select * from emp;

update emp
set comm=nvl(comm,0)+500
where comm is null;

rollback;
select * from emp;

select comm, nvl(comm,500) NVL_C, 
nvl2(comm,1000,6000) NVL2_C from emp;

select nvl(e.ename,'No Name'), nvl(e.job,'No Job'),
nvl(d.dname,'No Dept') from ee e full join dept d
on e.dno = d.deptno;

select e.ename, nvl(e.ename,'No Name'), e.job,nvl(e.job,'No Job'),
d.dname, nvl(d.dname,'No Dept') from ee e full join dept d
on e.dno = d.deptno;

select e.ename, e.job,d.dname from ee e full join dept d
on e.dno = d.deptno;