desc dual;

select * from dual;

select floor(-38.23),floor(-38), floor(38.23),floor(38) from dual;

select ceil(-38.23),ceil(-38), ceil(38.23),ceil(38) from dual;

select trunc(sysdate) from dual;

select sysdate from dual;

select * from desc feb_b2_emp

select * from dual;

 desc dual;
 
select sysdate from dual
where sysdate = to_date(sysdate,'dd-mon-y yyy hh:mi:ss');

alter session set nls_date_format = 'dd-mon-yyyy';

select sysdate from dual;

select sysdate Curr_Date, sysdate+1 Next_date from dual;

select sysdate, sysdate+1/24 from dual;

select sysdate, sysdate+1/24, sysdate+1/24/60, sysdate+1/24/60/60 from dual;

select sysdate+1/24/60/60 from dual;

select sysdate from dual;
 
select add_months(sysdate,-4) from dual;

select months_between(sysdate,'15 Oct 1981') from dual;
select abs(months_between('15 Oct 1981',sysdate)) from dual;

select round(months_between(sysdate,'15 Oct 1981')/12) from dual;
select round(sysdate) from dual;

select add_months(sysdate,5) from dual;
   --- some versions it gives an error
select round(months_between(sysdate,'15 Oct 1981')/12) Age from dual;

select round(months_between(sysdate,'10 July 2008')/12) Experience from dual;

select trunc(trunc(months_between(sysdate,'17-Oct-1982'))/12) from dual;

select ename,trunc(months_between(sysdate,hiredate)/12) Experience from ee;

select trunc(abs(months_between(sysdate,'18-Oct-2007'))/12) from dual;

select abs(months_between('18-Oct-2015',sysdate)) from dual;

select months_between(sysdate,'16-Oct-2015') from dual;

select months_between(sysdate,'16-Oct-2015') from dual;

select floor(Total_Months/12) Years, mod(Total_Months,12) from
(
select months_between(sysdate,'15-Oct-1981') Total_Months from dual
);

select next_day(sysdate,4) from dual;

select next_day(sysdate,'Tuesday') from dual;

select lpad(rpad('Uday',10,'*'),15,'%') from dual;
select lpad(rpad('Uday',15,'*'),3,'%') from dual;

select last_day(sysdate) from dual;

select to_char(sysdate,'d') from dual; 
--Day of week

select to_char(sysdate,'dd') from dual; 
--Day of Month

select to_char(sysdate,'ddd') from dual; 
--3 Digit day of year

select to_char(sysdate,'dy') from dual;
 --day name of week in short

select to_char(sysdate,'day') from dual;
--full day name of week in lowercase

select to_char(sysdate,'DAY') from dual; 
--full day name of week in Uppercase

select to_char(sysdate,'mm') from dual; 
--month of year in number 

select to_char(sysdate,'mon') from dual; 
--month name of year in short in lowercase

select to_char(sysdate,'MON') from dual;
--month name of year in short in Uppercase

select to_char(sysdate,'month') from dual;
--Full month name of year in lowercase

select to_char(sysdate,'MONTH') from dual;
--Full month name of year in Uppercase

select to_char(sysdate,'yy') from dual;
-- last 2 digits of year

select to_char(sysdate,'yyyy') from dual;
--year

select to_char(sysdate,'year') from dual;
--year

select to_char(sysdate,'w') from dual;
--1 digit week of the month

select to_char(sysdate,'ww') from dual;
--2 digit week of the year

select to_char(sysdate,'hh:mi:ss') from dual;

select to_char(sysdate,'ddd month year') from dual; 

select to_char(sysdate,'RM') from dual;

select to_char(sysdate+270,'rm') from dual;

select to_date('05-Oct-2015','dd mon yy') from dual;

SELECT SYSDATE+270 FROM DUAL;

select next_day(sysdate,2) from dual;

select next_day(sysdate,'Monday') from dual;

--Numeric Function:

select * from dual;

desc dual;

select abs(-123.23) ABS_VAL, mod(17,3) MOD_VAL, trunc(17/3,2) TRNC_VAL from dual;

select abs(123.23) from dual;

select mod(17,3) from dual;

select 17/3 from dual;

select trunc(17/3,2) from dual;

select trunc(1738.737) from dual;

select trunc(1738.137,2) from dual;

select trunc(17385.137,-1) from dual;

select trunc(1738.137,-4) from dual;

select trunc(1738.137,-3) from dual;

select round(1738.13463,2) from dual;
select round(1738.135,2) from dual;
select round(1738.134,-1) from dual;
select round(1738.134,-2) from dual;
select round(5738.134,-4) from dual;

select floor(38.35) from dual;
select floor(-38.50) from dual;

select ceil(38.25) from dual;
select ceil(-38.54) from dual;

select floor(48) from dual;
