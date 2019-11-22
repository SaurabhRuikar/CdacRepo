select * from src_emp;

create table src_emp as 
select * from ee
 insert into src_emp values(1200,'UD','MANAGER',7698,'17 Dec 2010',24000,null,20,'M');
 


select * from tgt_emp; 

drop table src_emp;

create table tgt_emp as 
select empno,ename,job,mgr,sal from src_emp
where 1=2;

truncate table tgt_emp;


alter table tgt_emp
add status varchar2(20);


merge into tgt_emp t using src_emp s
on (t.empno=s.empno)
when matched then
    update set
    t.ename=s.ename,
    t.job = s.job,
    t.mgr = s.mgr,
    t.sal = s.sal
when not matched then
    insert(t.empno,t.ename,t.job,t.mgr,t.sal)
    values(s.empno,s.ename,s.job,s.mgr,s.sal);



merge into tgt_emp t using src_emp s
on (t.empno=s.empno)
when matched then
    update set
    t.ename=s.ename,
    t.job = s.job,
    t.mgr = s.mgr,
    t.sal = s.sal,
    t.status = 'Updated'
when not matched then
    insert(t.empno,t.ename,t.job,t.mgr,t.sal,t.status)
    values(s.empno,s.ename,s.job,s.mgr,s.sal,'Inserted');
