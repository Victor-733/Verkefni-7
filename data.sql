create database 1611012220_Verkefni_7;
use 1611012220_Verkefni_7;

create table users(
    user varchar(35) primary key not null,
    pass varchar(35) not null,
    nafn varchar(35) not null
);

insert into users
values
    ('1611012220', 'mypassword', 'Victor_733');