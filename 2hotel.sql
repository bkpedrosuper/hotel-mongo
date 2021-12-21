-- HOSPEDE
create table hospede (
	codh integer NOT NULL,
	cpf char(11) NOT NULL,
	telefone character varying(15),
	nome character varying(50),
	email character varying(100),
	
	primary key(codh)
);

-- Nova Tabela
-- EMPREGADO
create table empregado (
	code integer NOT NULL,
	cpf char(11) NOT NULL,
	nome character varying(70) not NULL,
	pis char(11) NOT NULL,
	cargo character varying(25) NOT NULL,
	codg integer,
	numero integer,
	rua character varying(50),
	bairro character varying(25),
	
	primary key(code),
	foreign key (codg) references empregado on delete set null on update cascade
);

-- Nova Tabela
-- Quarto

create table quarto(
	codq integer NOT NULL,
	ramal integer,
	preco_dia decimal(10,2), 
	numero integer NOT NULL,
	andar integer NOT NULL,
	
	primary key(codq)
);


-- Nova Tabela
-- Reserva

create table reserva (
	codr integer not null,
	codq integer not null,
	numero_ocupantes integer,
	code integer,
	dt_entrada date,
	dt_saida date,
	
	primary key(codr),
	foreign key(code) references empregado(code) on delete set null on update cascade,
	foreign key(codq) references quarto(codq) on delete set null on update cascade
);

-- Nova Tabela
-- Contrato

create table contrato (
	codr integer not null,
	codh integer not null,
	
	foreign key(codr) references reserva(codr) on delete set null on update cascade,
	foreign key(codh) references hospede(codh) on delete set null on update cascade
);
