show databases;
create database register;
use register;
create table if not exists user (custid int not null auto_increment, Firstname varchar(15) not null, Lastname varchar(15) not null, Contactnumber varchar(12), Emailid varchar(35), Address varchar(300), primary key (custid));
select * from user;
alter table user auto_increment= 1;
delete from user where userid= 3;
drop table user;
#creating another table
create table if not exists fooditems (custid int, cust_id int auto_increment, Aloo_tikki_burger int not null, veggie_burger int not null, chicken_burger int not null, fries int not null, chicken_popcorn int not null,
cold_mojito int not null, cold_drink int not null, ice_cream_float int not null, mojito int not null, icecream int not null, Total int(8) not null, INDEX par_ind (cust_id),constraint fk_user foreign key (cust_id) references user (custid) on delete cascade on update cascade);

select * from fooditems;
select max(custid) from user;	
delete max(custid) from user;
update fooditems set Aloo_tikki_burger=12, veggie_burger=1, chicken_burger=1, fries=1, chicken_popcorn=1, cold_mojito=1, cold_drink=1, ice_cream_float=1, mojito=2, icecream=1, Total=5000 where cust_id = (select max(custid) from user);
drop table fooditems;
drop database register;