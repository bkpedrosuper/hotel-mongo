-- HOSPEDE
create sequence new_codh start 1;

create or replace function new_codh() returns trigger as
$$
declare
begin
	new.codh := nextval('new_codh');
	return new;
end;
$$
language plpgsql;

create trigger auto_codh before insert on hospede
	for each row execute procedure new_codh();

-- Nova Tabela
-- EMPREGADO
create sequence new_code start 1;

create or replace function new_code() returns trigger as
$$
declare
begin
	new.code := nextval('new_code');
	return new;
end;
$$
language plpgsql;

create trigger auto_code before insert on empregado
	for each row execute procedure new_code();

-- Nova Tabela
-- Quarto

create sequence new_codq start 1;

create or replace function new_codq() returns trigger as
$$
declare
begin
	new.codq := nextval('new_codq');
	new.ramal := 100*new.andar + new.numero;
	return new;
end;
$$
language plpgsql;

create trigger auto_codq before insert on quarto
	for each row execute procedure new_codq();

-- Nova Tabela
-- Reserva

create sequence new_codr start 1;
create or replace function new_codr() returns trigger as
$$
declare
begin
	new.codr := nextval('new_codr');
	new.numero_ocupantes = 0;
	return new;
end;
$$
language plpgsql;

create trigger auto_codr before insert on reserva
	for each row execute procedure new_codr();

-- Nova Tabela
-- Contrato

create table contrato (
	codr integer not null,
	codh integer not null,
	
	foreign key(codr) references reserva(codr) on delete set null on update cascade,
	foreign key(codh) references hospede(codh) on delete set null on update cascade
);

create or replace function new_contrato() returns trigger as
$$
begin
	update reserva set numero_ocupantes = numero_ocupantes+1 where codr = new.codr;
	return new;
end;
$$
language plpgsql;

create trigger auto_incrementa_ocupantes after insert on contrato
	for each row execute procedure new_contrato();