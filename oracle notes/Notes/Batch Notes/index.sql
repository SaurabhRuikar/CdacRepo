select * from user_indexes
where table_name='EE';

drop index pk_emp;

select * from ee
where empno=7499;

create index id11 on ee(empno);

explain plan for
select * from ee
where empno=7499;

select * from table(dbms_xplan.display());

create table er
(no number,
name varchar2(15)
);

alter table er
add constraint er_pk primary key(no);
alter table er
drop constraint er_pk;

create index idx1 on ee(empno);

drop index idx2;
desc emp;
commit;

select * from user_indexes
where table_name = 'EE';

select * from user_indexes
where table_name = 'EMP';

select * from user_indexes
where table_name = 'EMP1';


drop index pk_emp;

explain plan for
select * from emp
where empno=7566;

select * from table(dbms_xplan.display());

drop index idx3;

create index idx1 on emp(empno);

create unique index idx2 on emp1(ename);

create index idx3 on emp1(job, ename);

create index idx4 on ee(instr(ename,'A'));

explain plan for
select * from ee
where ename = 'ALLEN';

select * from table(dbms_xplan.display());

explain plan for
select * from emp1
where job in ('CLERK','MANAGER');

create unique index idx2 on ee(ename);

select * from ee where ename like 'A%';

select * from table(dbms_xplan.display());
select ename from ee;

explain plan for
select ename, instr(ename,'A') from ee
where instr(ename,'A')>0;

select * from table(dbms_xplan.display());

create bitmap index idx12 on ee(gender);
 
select * from ee where gender='M';

create index idx12 on ee(gender);

create or replace view m_v3
as
select * from ee;

update m_v3
set sal=sal+2000;


desc m_v3;
