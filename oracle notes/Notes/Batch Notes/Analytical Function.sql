  
select * from ee order by sal desc;

select empno, ename, sal,dno, 
rank() over(order by sal desc) as RNK,
dense_rank() over(order by sal desc) as D_RNK,
row_number() over(order by sal desc) as RNO
from ee;

select empno, ename, sal,
rank() over(partition by dno order by sal desc) as RNK,
dense_rank() over(partition by dno order by sal desc) as D_RNK,
row_number() over(order by sal desc) as RNO
from ee;


select empno, ename,sal,dno, 
rank() over(partition by dno order by sal desc) as RNK,
dense_rank() over(partition by dno order by sal desc) as D_RNK,
row_number() over(partition by dno order by sal desc) as RNO
from ee;

select empno, sal,dno, 
rank() over(order by sal desc) as RNK,
dense_rank() over(order by sal desc) as D_RNK,
row_number() over(order by sal desc) as RNO
from ee;

select  ename, dno, avg(sal) from ee
group by dno;

select ename, job,dno,sal, avg(sal) 
over(order by dno desc ) 
as AVG_SAL from ee;

select ename, job,dno,sal, avg(sal) 
over(partition by dno order by dno desc ) 
as AVG_SAL from ee;

select empno, ename, sal, job, dno, hiredate, 
dense_rank() over(order by sal desc) as NK
from ee

select  * from (select empno, ename, sal, job, dno, hiredate,
dense_rank() over(order by sal desc) as NK from ee)
where NK=7;

