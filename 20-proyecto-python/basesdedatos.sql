CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios(
  id		int(25) auto_increment not null,
  nombre	varchar(200),
  apellidos	varchar(200),
  email		varchar(255) not null,
  password	varchar(255) not null,
  fecha		date not null,
  CONSTRAINT	pk_usuario PRIMARY KEY (id),
  CONSTRAINT	uq_email UNIQUE (email)
)Engine=InnoDB;

CREATE TABLE notas(
  id		int(25) auto_increment not null,
  usuario_id	int(25) not null,
  titulo	varchar(255) not null,
  descripcion	MEDIUMTEXT,
  fecha		date not null,
  CONSTRAINT	pk_notas  PRIMARY KEY (id),
  CONSTRAINT	fk_nota_usuario FOREIGN key(usuario_id) REFERENCES usuarios(id)
)Engine=InnoDB;

