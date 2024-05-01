
drop table pessoa;
create table pessoa(
	id int auto_increment primary key,
    nome varchar(100),
    idade int,
    id_binary binary(16)
);

alter table pessoa add column nacionalidade varchar(100) not null default 'Brasileira';

insert into pessoa values (null,'Will', 35, uuid_to_bin('739b07f5-7293-4b35-ad05-699d356fe429'));
insert into pessoa values (null,'Chloe', 7, uuid_to_bin('d9f2c28f-25b8-45d1-8a48-37197c2065fc'));
insert into pessoa values (null,'Magie', 36, uuid_to_bin('28899fe8-2374-4271-b178-67066b472209'));

alter table pessoa drop column data_criacao;

insert into pessoa values (null,'Yuyu', 30, uuid_to_bin(UUID()),'Indiana');
insert into pessoa values (null,'Pocoyo', 7, uuid_to_bin(UUID()),'Indiana');
insert into pessoa values (null,'Chocoline', 7, uuid_to_bin(UUID()),'Chines');
insert into pessoa values (null,'Barriga', 20, uuid_to_bin(UUID()),'Japones');
