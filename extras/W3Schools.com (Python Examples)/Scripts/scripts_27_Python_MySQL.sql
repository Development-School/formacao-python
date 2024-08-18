
truncate table mydatabase.customers;
select * from mydatabase.customers;

drop table mydatabase.customersTMP;
create table mydatabase.customersTMP as
select * from mydatabase.customers;

select * from mydatabase.customersTMP;

create table mydatabase.users(
	id   int NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT NULL,
    fav  varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
);

# truncate table mydatabase.users;

insert into mydatabase.users values(1, 'John', 1);
insert into mydatabase.users values(2, 'Peter', 1);
insert into mydatabase.users values(3, 'Amy', 2);
insert into mydatabase.users (id, name) values(4, 'Hannah');
insert into mydatabase.users (id, name) values(5, 'Michael');

commit;

select * from mydatabase.users;

# ---

create table mydatabase.products(
	id   int NOT NULL AUTO_INCREMENT,
    name varchar(255) DEFAULT NULL,    
    PRIMARY KEY (id)
);

insert into mydatabase.products values(1, 'Chocolate Heaven');
insert into mydatabase.products values(2, 'Tasty Lemons');
insert into mydatabase.products values(3, 'Amy', 155);

commit;

select * from mydatabase.products;
