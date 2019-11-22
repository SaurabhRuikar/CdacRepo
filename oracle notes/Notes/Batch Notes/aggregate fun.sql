select max(sal) from ee;

select dno,gender, max(sal),min(sal) , avg(sal), sum(sal), count(sal) 
from ee
group by dno, gender;

order by dno
select deptno, max(sal),min(sal) , avg(sal), sum(sal), count(sal) from emp
group by deptno;



select count(*), count(sal), count(comm) from emp;

select gender, count(*), dno from ee
group by gender,dno;

select count (unique job ) from ee;

select dno, count (distinct job) from ee
group by dno;

select count(*), dno, max(sal) from ee
group by dno
having count(*)<5;

select * from ee

SELECT ROWID AS rd,ROWNUM,  ENAME, JOB, EMPNO,SAL, DNO FROM EE
WHERE ROWNUM<13



