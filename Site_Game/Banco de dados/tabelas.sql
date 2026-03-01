use game;/* Lógico_1: */

CREATE TABLE if not exists jogos (
    id_jogos int auto_increment primary KEY,
    nome char(255) not null,
    tipo char(255)
    
);


    
CREATE  TABLE if not exists endereco (
    id_endereco int auto_increment primary key,
    logradouro char(255) not null,
    bairro char(255) not null,
    cidade char(255) not null,
    estado char(255) not null,
    numero int not null
);


create table if not exists usuario(
	id_usuario int auto_increment primary key,
    nome char(255) not null,
    username varchar(50) not null,
    genero varchar(1),
    data_nascimento date not null,  
    senha text not null,
    nivel int,
    id_endereco int,
    foreign key(id_endereco) references endereco(id_endereco)
    on delete cascade);

CREATE TABLE if not exists joga (
    id_usuario int ,
    id_jogos int,
    foreign key (id_usuario) references usuario(id_usuario),
    foreign key (id_jogos) references jogos(id_jogos)
    on delete restrict
);


CREATE TABLE if not exists historico (
    id_usuario int,
    id_jogos int,
    vitorias int,
    derrotas int,
    soma_jogos int,
    soma_vitorias int,
    soma_derrotas int,
    foreign key (id_jogos) references jogos(id_jogos),
    foreign key (id_usuario) references usuario(id_usuario)
     
);
 show tables;
-- drop table joga,usuario,historico,endereco,jogos