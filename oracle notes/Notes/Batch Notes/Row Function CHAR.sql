desc dual;

select * from dual;

select length('UDAY') from dual;

select length('UDAY') STRLEN from dual;


select eno, ename, length(ename) as "Length Size" from feb_b1_emp;

select length('Swarit'), upper('Uday'), lower('UDay'), 
initcap('uday YAShwant deshMUKH') from dual;

select length(ename), upper(ename), lower(ename), 
initcap(ename) from ee;


select lpad(ename ,10,'*') from ee;
select lpad(ename ,4,'*') from ee;

select rpad(ename ,10,'*') from feb_b1_emp;

select length(trim('  Uday  ')) as A,
length(rtrim('  Uday  ')) as B,
length('  Uday  ') as C,
length(ltrim('  Uday  ')) D 
from dual;

select replace('Nik hil',' ', null) from dual;
select replace('abcaapqraaxyzaastuamnoaa','aa','%') from dual;

select reverse('12345') from dual;

select concat('Uday','Deshmukh') from dual;



select INSTR('Welecome to PSOUG.org','O') from dual
select INSTR('Welecome to PSOUG.org','o',1,1) from dual
select INSTR('Welecome to PSOUG.org','o',6,1) from dual
select INSTR('Welecome to PSOUG.org','o',1,2) from dual
select INSTR('Welecome to PSOUG.org','o',1,3) from dual


select INSTR('Welecome to PSOUG.org','o',-1,3) from dual
select INSTR('Welecome to PSOUG.org','o',-17,3) from dual

select SUBSTR('Welecome to PSOUG.org',1,6) from dual
select SUBSTR('Welecome to PSOUG.org',1,3) from dual
select SUBSTR('Welecome to PSOUG.org',2) from dual

select SUBSTR('Welecome to PSOUG.org',-1,3) from dual
select SUBSTR('Welecome to PSOUG.org',-16,3) from dual

select ename from emp where instr(ename,'A')>0;
