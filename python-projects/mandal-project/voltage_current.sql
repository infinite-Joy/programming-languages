drop table if exists voltage_current;

create table voltage_current (ID INTEGER PRIMARY KEY, voltage real, current real, Timestamp DATETIME DEFAULT strftime('%s', 'now'));

insert into voltage_current (ID, voltage, current) values (1, 1.0, 2.0);
insert into voltage_current (ID, voltage, current) values (2, 2.0, 4.0);
insert into voltage_current (ID, voltage, current) values (3, 3.0, 9.0);
