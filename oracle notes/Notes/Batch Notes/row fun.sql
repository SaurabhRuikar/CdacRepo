desc dual;

select * from dual;

select length('UDAY') as "Length Size" from dual;

select empno, ename, length(ename) as "Length Size" from emp;

select length('uday YAShwant deshMUKH'), 
upper('uday'), 
lower('YAShwant'), 
initcap('uday YAShwant deshMUKH') 
from dual;

select lpad(ename ,4,'*') from emp;

select rpad(ename ,10,'*') from feb_b1_emp;

select length(trim('  Uday  ')),
length(ltrim('Uday','U')),
length(rtrim('  Uday','y')) 
from dual;

select replace('Nik hil',' ', null) from dual;
select replace('abcaapqraaxyzaastuamnoaa','aa','%') from dual;

select reverse('12345') from dual;

select concat('Uday ','Deshmukh') from dual;

sunstr

select INSTR('Welecome to PSOUG.org','O') from dual
select INSTR('Welecome to PSOUG.org','o',1,1) from dual
select INSTR('Welecome to PSOUG.org','o',6,1) from dual
select INSTR('Welecome to PSOUG.org','o',6,3) from dual
select INSTR('Welecome to PSOUG.org','o',1,2) from dual
select INSTR('Welecome to PSOUG.org','o',7,3) from dual


select INSTR('Welecome to PSOUG.org','o',-1,3) from dual
select INSTR('Welecome to PSOUG.org','o',-17,3) from dual

select SUBSTR('Welecome to PSOUG.org',1,6) from dual
select SUBSTR('Welecome to PSOUG.org',1,3) from dual
select SUBSTR('Welecome to PSOUG.org',2) from dual

select SUBSTR('Welecome to PSOUG.org',-1,3) from dual
select SUBSTR('Welecome to PSOUG.org',-17,3) from dual
select SUBSTR('Welecome to PSOUG.org',-21,3) from dual

select ename from ee where instr(ename,'A')>0;


select 
INSTR('Welecome to PSOUG.org','o',INSTR('Welecome to PSOUG.org','o',1,1)+1,1),
        INSTR('Welecome to PSOUG.org','o',1,1),
substr('Welecome to PSOUG.org',INSTR('Welecome to PSOUG.org','o',1,1),INSTR('Welecome to PSOUG.org','o',INSTR('Welecome to PSOUG.org','o',1,1)+1,1)-INSTR('Welecome to PSOUG.org','o',1,1))
         from dual