select * from cust_act_dts;
select * from acc_type;
select * from cust_dts;

select * from emp1;
select * from sd;
select * from locations;

select * from comp;
select * from prod;
select * from discount;

select * from ee;
select * from dept;

select * from ee, dept;

select * from comp inner join prod
on comp.cid=prod.cid;

select * from comp natural join prod;

select * from emp1 natural join sd;

select * from ee natural join dept;

select * from emp1 join sd
using (deptno);

select * from ee, dept
where ee.dno=dept.deptno;

select * from ee, dept
where ee.dno=dept.deptno
and dept.dname='ACCOUNTING';

select ename from ee, dept
where dname = 'ACCOUNTING' and ee.dno = dept.deptno

select e.*,d.* from ee e, dept d
where e.dno <> d.deptno

select * from ee, dept
where EE.DNO=DEPT.DEPTNO;

select e2.ename, e2.dno from ee e1, ee e2
where e1.ename='ALLEN' and e1.dno=e2.dno;

select e2.ename, e2.job from ee e1, ee e2
where e1.ename='ALLEN' and e1.job=e2.job;

select e2.ename, e2.mgr from ee e1, ee e2
where e1.ename='ALLEN' and e1.mgr=e2.mgr;

select * from ee
where empno=7698

select * from ee, dept
where dept.dname = 'ACCOUNTING'
and EE.DNO=DEPT.DEPTNO;

select * from ee inner join dept
on EE.DNO=DEPT.DEPTNO
where dept.dname = 'ACCOUNTING';

select * from ee natural join dept

select * from emp1 natural join dept;

select * from emp1 join sd
using (mgr);

select * from ee, dept
where dept.dname in ('SALES','RESEARCH')
and EE.DNO=DEPT.DEPTNO;

select dname from ee, dept
where ee.ename = 'ALLEN'
and EE.DNO=DEPT.DEPTNO;

select dname from ee, dept
where EE.DNO=DEPT.DEPTNO 
and ee.ename = 'ALLEN';


select empno, ename, job,dno, deptno, dname from ee, dept;
 
select dname from ee, dept
where ee.dno=DEPT.DEPTNO and ee.ename = 'ALLEN';

select ename, job, dname from ee, dept
where ee.dno<DEPT.DEPTNO; 

select dname from ee, dept
where ee.ename = 'ALLEN' and ee.dno=DEPT.DEPTNO ;


select * from comp;
select * from prod;
select * from discount;

insert into discount values('d1','First','15%');
insert into discount values('d2','Middle','10%');
insert into discount values('d3','Last','5%');

select * from incr_tab;

select * from user_tables;

select cid, pname, pid, pcost, disid,disname,disperc from
prod, discount
where pname like '%TV%' and disname = 'Middle';

commit;

-- Equi Join

select e.*, d.* from ee e, dept d
where d.dname = 'ACCOUNTING' and e.dno = d.deptno;

select e.*, d.* from ee e inner join dept d
on e.dno = d.deptno
where d.dname = 'ACCOUNTING' ;

-- select ee.*, dept.* from ee inner join dept

select * from emp1 natural join dept 

select e.*, d.* from ee e, dept d
where e.dno = d.deptno and d.dname = 'ACCOUNTING';


select e.*, d.* from ee e inner join dept d
on e.dno = d.deptno
where d.dname = 'ACCOUNTING' ;

select * from comp;
select * from prod;
select * from discount;

select * from comp natural join prod;

select * from emp1;
select * from sd;

select * from emp1 natural join sd;

select * from emp1 join sd
using (deptno);


-- SYNTAX FOR OUTER JOIN IN ANSI SQL

-- LOJ


select nvl(c.cname,'No Comp'), nvl(p.pname,'No PD'),P.PCOST,
p.pid, c.cid select comp.*, prod.* from comp left join prod
on comp.cid=prod.cid;
from comp c left join prod p
on c.cid=p.cid;


select nvl(c.cname,'No Comp'), nvl(p.pname,'No PD'),P.PCOST,
p.pid, c.cid from comp c right join prod p
on c.cid=p.cid;


-- ROJ

select * from comp left join prod
on comp.cid=prod.cid;

-- FOJ

select comp.*, prod.* from comp full join prod
on comp.cid=prod.cid;
 
select * from abc;

select name from abc

select n1.nm from abc n1, abc n2
where n1.nm='A' and n1.city=n2.city;

-- SYNTAX FOR OUTER JOIN IN SQL PLUS

-- LOJ

select comp.*, prod.* from prod inner join comp
on prod.cid(+)=comp.cid;

-- ROJ

select comp.*, prod.* from comp inner join prod
on prod.cid=comp.cid(+);

-- FOJ

select comp.*, prod.* from comp inner join prod
on prod.cid(+)=comp.cid
union
select comp.*, prod.* from comp inner join prod
on prod.cid=comp.cid(+);

-- SubQuery

select dname from dept  
where  deptno in 
( select dno from ee 
    where empno in (7788,7566, 7698));

select dname from dept  
where  deptno =( select dno from ee 
    where ename ='ALLEN'); 

select * from dept
where deptno in (select dno from ee where job='MANAGER');

select * from ee;


select * from acc_type;
select * from cust_dts;
select * from cust_act_dts;

select act.act_t, cd.cname,cd.city,cad.act_bal, cad.acc_no  
from acc_type act, cust_dts cd,
cust_act_dts cad
where ACT.ACT_T=CAD.ACT_T and
CD.CNO=CAD.CNO;

select act.act_t from acc_type act, cust_dts cd,
cust_act_dts cad
where CD.CNAME = 'Swarit' and
ACT.ACT_T=CAD.ACT_T and
CD.CNO=CAD.CNO;

                                                                    
select act.act_t, cd.cname,cd.city,cad.act_bal, cad.acc_no  
from acc_type act, cust_dts cd,
cust_act_dts cad
where ACT.ACT_T=CAD.ACT_T and
CD.CNO=CAD.CNO and cd.gender='M';

select act_name from acc_type act, cust_dts cd,
cust_act_dts cad
where cd.cname = 'Kiran' and ACT.ACT_T=CAD.ACT_T and
CD.CNO=CAD.CNO;

select act_name from acc_type act inner join
cust_act_dts cad
on ACT.ACT_T=CAD.ACT_T 
inner join cust_dts cd
on CD.CNO=CAD.CNO
where cd.cname = 'Anshit';

select count(*) from ee e, dept d
where e.dno = d.deptno and d.dname ='RESEARCH';

select act_name from acc_type where
act_t=(select act_t from cust_act_dts 
where cno=
(select cno from cust_dts where cname='Anshit'));

select act_name from acc_type where
act_t=(select act_t from cust_act_dts 
where cno=6);

select act_name from acc_type where
act_t='SAL';

SELECT * FROM CUST_DTS WHERE CNO in
(SELECT CNO FROM CUST_ACT_DTS WHERE ACT_T
in (SELECT ACT_T FROM ACC_TYPE WHERE ACT_T='SB'));

SELECT * FROM CUST_DTS WHERE CNO in
(SELECT CNO FROM CUST_ACT_DTS WHERE ACT_T='SB');

select * from tab;
