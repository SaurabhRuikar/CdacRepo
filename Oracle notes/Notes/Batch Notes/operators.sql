SELECT * FROM EMP1;

SELECT ENAME, SAL,JOB FROM EMP1;

SELECT ENAME, SAL,JOB FROM EMP1
WHERE JOB='Manager'; y7hhhhhhhhhhhb 

select * from emp1;

select * from ee
where sal >= 5000;

select * from ee
where sal between 5000 and 15000;

select * from ee
where sal >=5000 and sal <=15000;

select * from ee
where job = 'MANAGER' or job = 'SALESMAN';

select * from ee
where job in ('MANAGER','SALESMAN') and sal between 5000 and 10000;

select * from ee
where job<>'MANAGER' and job<>'SALESMAN' ;

select * from ee
where job not in ('MANAGER','SALESMAN');

select * from emp1;

select * from emp1
where comm is null;

select * from emp1
where comm is not null;

select * from ee
where ename like 'A%';

select * from ee
where ename like '%ES%';

select * from ee
where ename like '%LL%';

select * from ee
where ename like 'A_A%';


select * from emp1;

select * from emp1
where job = 'CLERK';

select * from emp1
where deptno ^= 10;

select * from emp1
where job = 'CLERK' and sal >1000;

select * from emp1
where job in ('MANAGER','CLERK','SALESMAN');

select * from emp1
where job in ('MANAGER','CLERK','SALESMAN') and 
sal between 2000 and 4000;

select sal, deptno,job,ename from emp1
where sal <= 5000;

select sal, deptno,job,ename from emp1
where sal between 2000 and 4000 and deptno!=20;

select sal, deptno,job,ename from emp1
where job!='MANAGER';

select * from emp1
where comm is not null;

select * from emp1
where comm is null or comm = 0;
 
select * from emp1
where comm >0;

select distinct job, distinct deptno from emp1;

select unique job from emp1;

select * from emp1
where ename like 'S%H';

select * from emp1
where ename like '%LL%';

select * from emp1
where ename like '%ES';

select * from emp1
where ename like 'F___';

select * from emp1
where ename like '____';

select * from emp1
where ename like 'A_A%';

