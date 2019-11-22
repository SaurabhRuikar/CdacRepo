-- Constraints:
-----------------------------

-- It is rule/protocol apply on column of a table.
-- Due to it you have restrictions to add data in a table.

-- Types of Constraints:
    -- 1) Primary Key Constraints
    -- 2) Foreign Key Constraints
    -- 3) Check Constraints
    -- 4) Not Null Constraints
    -- 5) Unique Key Constraints
    
    -- 6) Default Constraints
--------------------------------------------------------------

-- 1) Primary Key Constraints:
            Primary Key:    -- It is a candidate key
                            -- It is uniquely identify the records
                            -- It must be not null.
                          -- One table have one and only one PK.
            Candidate Key:-- If one table have one or more than one columns have
                            ability to became a primary key then those keys are
                            called as Candidate keys.
                          -- One Table have one or more than one 
                            candidate Keys.
         
WAYS OF CONSTRAINTS THAT ARE APLLIED ON A COLUMN OF A TABLE:
-- COLUMN LEVEL:
        -- With Constraint Name 
        -- Without Constraint Name
-- TABLE LEVEL
-- USING ALTER LEVEL

drop table ab;

CREATE TABLE ab
(
   no   NUMBER(3) ,
   nm   VARCHAR2(10)
);

alter table ab
add constraint ab_no_pk primary key(no);

select * from user_constraints
where table_name = 'AB';

select * from ab;

alter table ab
add constraint gsp primary key(no);

alter table ab
drop constraint SYS_C0015622;

  DROP TABLE ab;
  TRUNCATE TABLE ab;

INSERT INTO ab
  VALUES   (1, 'ud');

INSERT INTO ab
  VALUES   (2, 'cd');

INSERT INTO ab
  VALUES   (null, 'rd');

INSERT INTO ab
  VALUES   (2, 'td');

alter table ab
add constraints ab_no_pk primary key (no);

SELECT   *
  FROM   user_constraints
 WHERE   table_name = 'AB';

ALTER TABLE ab
DROP CONSTRAINT SYS_C0013334;

 alter table ab
 drop constraint ab_no_pk

 jan_select * from ab;

 ALTER TABLE ab
 ADD CONSTRAINT ab_no_pk PRIMARY KEY(no);


-- 2) Unique Key Constraints:
            Unique Key:     -- It is uniquely identify the records
                            -- It accepts null values.
                          -- One table have one and more UK.
            
WAYS OF CONSTRAINTS THAT ARE APLLIED ON A COLUMN OF A TABLE:
-- COLUMN LEVEL:
        -- With Constraint Name 
        -- Without Constraint Name
-- TABLE LEVEL
-- USING ALTER LEVEL

create table a1
 (
 no number,
 mob number(10) unique,     -- Column Level With out Constraint Name
 nm varchar2(10) constraint hfhf not null
 );

DROP table A1;
 
 alter table a1
 drop constraints SYS_C0013485
 
 SELECT   *
  FROM   user_constraints
 WHERE   table_name = 'A1';

 create table a1
 (
 no number,
 mob number(10) constraint UK unique, -- Column Level With Constraint Name
 nm varchar2(10)
 );
 
 desc a1;
 
 drop table a1;

alter table a1
drop constraint HFHF;


drop constraint SYS_C0015286
add constraint hf unique(mob);
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10),   -- Table Level With Constraint Name
 constraint a1_mob_uk unique(mob)
 );
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10) not null,   -- Table Level With Constraint Name
 constraint a1_mob_uk unique(mob),
 constraint a1_no_pk primary key(no)
 );
 
 drop table a1;
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10) not null   
 );
 
 -- Alter Level With Constraint Name
  
 alter table a1
 add constraint UK unique(mob);

INSERT INTO A1 VALUES(1,1234,null);
INSERT INTO A1 VALUES(2,1234,'ad');
INSERT INTO A1 VALUES('2','12','ad');
INSERT INTO A1 VALUES(2,NULL,null);
,(12,123456,'ad1') );
INSERT INTO A1 VALUES(1,1234,'ad');

INSERT INTO A1(NO, MOB) VALUES(5,123456789);

truncate table a1;

ALTER TABLE a1
DISABLE CONSTRAINT UK;

ALTER TABLE a1
ENABLE CONSTRAINT UK;

delete from a1
where mob =1234;

ROLLBACK;


DELETE FROM A1 WHERE MOB=1234;
SELECT * FROM A1;


SELECT * FROM ab;

 ALTER TABLE ab
 DISABLE CONSTRAINT ab_no_pk;
 ALTER TABLE ab
 ENABLE CONSTRAINT ab_no_pk;

desc ab;

SELECT   * FROM jan_b2_e;

alter table jan_b2_e
rename to we_e

alter table jan_b2_d
rename to we_d

select * from we_e;
select * from we_d;

alter table we_e
drop constraint JAN_DEPTNO_RK;

alter table we_d
drop constraint JAN_DEPTNO_PK;

alter table we_e
drop constraint JAN_EMPNO_PK;

select * from user_constraints
where table_name in('WE_E','WE_D');

alter table we_d
add constraint we_d_pk primary key(deptno);

alter table we_e
add constraint we_e_pk primary key(empno);

select * from we_e;

update we_e
set deptno=40
where empno=3000;

alter table we_e
add constraint we_e_rk foreign key(deptno) references we_d(deptno);

alter table we_e
drop constraint WE_E_RK;

alter table we_e
add constraint we_e_rk foreign key(deptno) references we_d(deptno)
on delete set null;

select * from we_e;
select * from we_d;

alter table we_e
add constraint we_e_rk foreign key(deptno) references we_d(deptno)
on delete cascade;


delete from we_d
where deptno=30;

delete from we_e
where deptno=30;

rollback;


SELECT   * FROM jan_b2_d;




CREATE TABLE jan_b2_e1
AS
   SELECT   * FROM ee;

CREATE TABLE jan_b2_d1
AS
   SELECT   * FROM dept;

SELECT   * FROM jan_b2_e1;

SELECT   * FROM jan_b2_d1;

 ALTER TABLE jan_b2_d1
 ADD CONSTRAINT jan_deptno_pk PRIMARY KEY(deptno);
 ALTER TABLE jan_b2_e1
 ADD CONSTRAINT jan_empno_pk PRIMARY KEY(empno);
 ALTER TABLE jan_b2_e1
 ADD CONSTRAINT jan_deptno_rk FOREIGN KEY(deptno)
 REFERENCES jan_b2_d1(deptno);

SELECT * FROM jan_b2_E1;

DELETE FROM   jan_b2_d1
      WHERE   deptno =(20);

 ALTER TABLE jan_b2_e1
 DROP CONSTRAINTS jan_deptno_rk;
 ALTER TABLE jan_b2_e1
 ADD CONSTRAINT jan_deptno_rk FOREIGN KEY(deptno)
 REFERENCES jan_b2_d1(deptno)
 ON DELETE SET NULL;

SELECT   *
  FROM   user_constraints
 WHERE   table_name = 'JAN_B2_E';

ROLLBACK;
 ALTER TABLE jan_b2_e
 ADD CONSTRAINT jan_deptno_rk FOREIGN KEY(deptno)
 REFERENCES jan_b2_d(deptno)
 ON DELETE CASCADE;

UPDATE   jan_b2_e
   SET   deptno = 40
 WHERE   deptno IS NULL;

 ALTER TABLE jan_b2_e
 DROP CONSTRAINTS jan_empno_pk, jan_deptno_rk;
  
 
 drop table a1;
 
 -- Column level without constraint name
 
 drop table a1;
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10) not null  
 );
 
 select * from user_constraints
 where table_name= 'A1';
 
 -- Column level with constraint name
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10) constraint a1_nm_nl not null  
 );
 
 select * from user_constraints
 where table_name= 'A1';
 
 -- Table level with constraint name is not possible by not null
 
 drop table a1;
 
 create table a1
 (
 no number,
 mob number(10),
 nm varchar2(10), 
 constraint a1_nm_nl not null(no)  
 );
 
 select * from user_constraints
 where table_name= 'A1';
 
 -- Check constraints
 
 drop table a1;
 
 create table a1
 (
 no number check (no>0),
 mob number(10),
 nm varchar2(10),
  esal number(7,2)
  );
 
  constraint a1_esal_cc check (esal>5000),
  constraint a1_no_cc check (no>0)
 
 
 select * from user_constraints
 where table_name= 'A1';
 
 truncate table a1;

    alter table a1
    add constraint a1_no_chk check (no>0);
     
 insert into a1 values(1,1234,'UD',4500);
 insert into a1 values(0,1234,'UD',500);
 
 create table a1
 (
 no number primary key,
 mob number(10),
 nm varchar2(10) constraint a11 check (upper(nm)),
  esal number(7,2),
  constraint a1_esal_cc check (esal>5000)
 );
  
 
 drop table a1;
 
 create table a1
 (
 no number primary key,
 mob number(10),
 nm varchar2(10) default 'UDUD'
 );
  
 insert into a1 values(3,1212,'uf');
 insert into a1 values(2,1222,'sdfsf');
 insert into a1(no,mob) values(1,1212);
 
 select * from a1;
 
 DROP TABLE A1;
 
 create table a1
 (
 no number primary key,
 mob number(10) DEFAULT 8888888888,
 nm varchar2(10)
 );
 
 alter table a1
 modify mob default 1234;
 
 select * from user_constraints
 where table_name= 'A1';
 
 insert into a1 values(1,123456,'UDAY');
 insert into a1 values(1,'UDAY');
 insert into a1 (no,mob,nm)values(1,  ,'UDAY');
  insert into a1 (no,nm)values(6,'UDAY');
select * from a1;
 



create table m_m2
(
eno number check (eno>0),
nm varchar2(10) not null,
mob number constraint UK1 unique,
job varchar2(10) check (job in ('C','M','S')),
constraint m11_eno_pk primary key(eno)
);

insert into m_m2 values(1,'UDAY',123456,'C');
insert into m_m2 values(2,'UDAY1',12345,'c');
insert into m_m2 values(4,,123,'M');
insert into m_m2 values(1,'UDAY',123456,'C');

alter table m_m2
add constraint kjkjk not null(job);

Reference Key:
-----------------------

create table m_sec_emp
as
select * from emp1;

create table m_pri_dept
as
select * from dept;

select * from m_sec_emp;
select * from m_pri_dept;

drop table m_sec_emp;
drop table m_pri_dept;

alter table m_pri_dept
add constraint m_pri_dept_deptno_pk primary key(deptno);

alter table m_sec_emp
add constraint m_sec_emp_empno_pk primary key(empno);

alter table m_sec_emp
add constraint m_sec_emp_deptno_rk foreign key(deptno) 
references m_pri_dept(deptno);

delete from m_sec_emp
where ename= 'ALLEN';

delete from m_pri_dept
where deptno=10;

select * from m_sec_emp;

rollback;

alter table m_sec_emp
drop constraint m_sec_emp_deptno_rk;

alter table m_sec_emp
add constraint m_sec_emp_deptno_rk foreign key(deptno) 
references m_pri_dept(deptno)
on delete set null;

alter table m_sec_emp
add constraint m_sec_emp_deptno_rk foreign key(deptno) 
references m_pri_dept(deptno)
on delete CASCADE;


rollback;