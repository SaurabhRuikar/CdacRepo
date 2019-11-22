select abs(-17.25) from dual

select round(-45.40),round(-45.60) from dual

select round(45.40),round(45.60) from dual

select mod(-45,6) from dual;


select round(65.926,-2),round(459.924,-1) from dual

select trunc(45.40),trunc(45.60) from dual

select trunc(454.926,-2),trunc(422.924,-2) from dual

select trunc(45.926,-1),trunc(45.924,-1) from dual

select floor(38.45), floor(-38.45) from dual

select ceil(67.70), ceil(-99.50) from dual

select round(269.325,-2) from dual

select sysdate from dual

insert into rahul1_test values(1,'Amit',1000,to_date('1 01 2015','dd mm yyyy'))

select to_char(jn_dt,'ddd month year') from rahul1_test 

select to_char(jn_dt,'RM') from rahul1_test

select to_char(jn_dt,'ww') from rahul1_test

select to_char(jn_dt,'w') from rahul1_test

select to_char(jn_dt,'IW') from rahul1_test

select to_char(jn_dt,'DAY') from rahul1_test

select to_char(jn_dt,'DY') from rahul1_test

select to_char(sysdate,'MI') from dual

select to_char(sysdate,'ss') from dual

select to_char(sysdate,'ssss') from dual

select rOUND(MONTHS_BETWEEN('11-JAN-2013','01-JAN-2012')) FROM DUAL

SELECT TO_CHAR(ADD_MONTHS('11-JAN-2015',6),'DD MON YYYY') FROM DUAL

SELECT NEXT_DAY('23-AUG-2015','TUESDAY') FROM DUAL

SELECT LAST_DAY('01-MAR-2013') FROM DUAL

-- nvl and nvl2 functions:

SELECT COMM,NVL(COMM,0) as NV,NVL2(COMM,'Value','Null') as NV2 FROM EE;

select comm from ee;

UPDATE EE
SET COMM = NVL(COMM,0)+500;

 ROLLBACK;

UPDATE EE
SET COMM = NVL2(COMM,COMM+500,500);
 
update ee
set comm=nvl(comm,0)+1000;
rollback;

select comm, nvl(comm,100), nvl2(comm,'yes','no') from emp1;

update emp1
set comm= nvl(comm,0)+100;

select * from emp1;

create table emp as select * from emp1; 

SELECT NULLIF('1','1'),NULLIF('2','1'),NULLIF('1','2') FROM DUAL

SELECT NULLIF(0,0),NULLIF('null','1'),NULLIF('1','2'),NULLIF('null','null') FROM DUAL

SELECT COALESCE('1','2','3'),COALESCE(NULL,2,3),COALESCE(NULL,NULL,3), 
COALESCE(NULL,NULL,NULL), COALESCE(0,0,0), COALESCE(1,1,1), 
COALESCE(0,null,0) FROM DUAL

select * from tab;

SELECT COALESCE('1','2','3') ,COALESCE(NULL,'2','3'),COALESCE(NULL,NULL,'3') FROM DUAL