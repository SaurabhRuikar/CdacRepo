select * from  ss;

create table gs
(
    A number
);

create table s
(
    B number
);

drop table s;

 insert into s values(11);
  insert into s values(12);
    insert into s values(null);
 insert into s values(16);
  insert into s values(17);
    insert into s values(18);

select * from s;
select * from gs;

insert into gs values(11);
  insert into gs values(12);
    insert into gs values(null);
insert into gs values(13);
  insert into gs values(14);
    insert into gs values(15);

delete from gs
where A is null
  
  select * from gs
  intersect
  select * from s;

select A from gs
  union
  select B from s;

select A from gs
  union all
  select B from s;
  
  select A from gs
  minus
  select B from s;

select B from s
  minus
  select A from gs;

Suppose we have three branches B1, B2 and B3

-- Get Cust Details from all Branches
-- Common Cust from last two branches
-- Unique cust from branch 1(B1)

create table cust_b1
( 
cid varchar2(5),
cname varchar2(10),
caddr varchar2(10),
cmob number(10),
cgender varchar2(1)
);

create table cust_b2
( 
cid varchar2(5),
cname varchar2(10),
caddr varchar2(10),
cmob number(10),
cgender varchar2(1)
);

create table cust_b3
( 
cid varchar2(5),
cname varchar2(10),
caddr varchar2(10),
cmob number(10),
cgender varchar2(1)
);

insert into cust_b1 values('c1','a','Pune',1212,'M')

insert into cust_b3 values('c1','a','Pune',1212,'M')

insert into cust_b1 values('c1','a','Pune',1212,'M')


insert into cust_b2 values('c2','b','Nashik',1990,'F')

insert into cust_b1 values('c2','c','Pune1',2121,'M')

insert into cust_b1 values('c3','z','Pune2',8888,'F')

insert into cust_b2 values('c4','a','Pune',1212,'M')

insert into cust_b3 values('c5','p','Nagar',12,'F')

insert into cust_b3 values('c4','a','Pune',1212,'M')

select * from cust_b1;
select * from cust_b2;
select * from cust_b3;

select * from cust_b1
union 
select * from cust_b2
union 
select * from cust_b3

select * from cust_b1
union all
select * from cust_b2
union all
select * from cust_b3

select * from cust_b1
minus
(select * from cust_b2
union all
select * from cust_b3)

select * from cust_b1
minus
(select * from cust_b2
union all
select * from cust_b3);

select * from cust_b1
minus
select * from cust_b2
minus
select * from cust_b3;

select * from cust_b2
intersect
select * from cust_b3;


select * from cust_b1;

select cid, cname,cmob from cust_b1;

select cid,cmob,cgender, cname,caddr, rowid as ID, rownum  from cust_b1;

select cid,cmob,rownum, cname  from cust_b1;

select cid,cmob,rownum, cname  from cust_b1 order by cname;

create table tt
(
    birth_date date check( birth_date between date '1900-01-01' and
    date '2011-12-08')
);


drop table tt;
select 'HI' from dual
where 'HI'is null;

select count(*) from ee
where comm> any(select comm from ee);

select count(*) from ee
where sal> any(select sal from ee);


select * from ee;
select * from dept;

select * from ee,dept;
