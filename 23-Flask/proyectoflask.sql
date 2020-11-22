CREATE DATABASE IF NOT EXISTS proyectoflask;
USE proyectoflask;

CREATE TABLE coches (
  id		int(255) auto_increment,
  marca	    varchar(255),
  modelo	varchar(255),
  precio	float,
  ciudad    varchar(255),
  created_at TIMESTAMP,
  PRIMARY KEY (id)
) Engine=InnoDB;


