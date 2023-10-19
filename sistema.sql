create DATABASE if not exists Barcelona;
use Barcelona;
create table futbolistas(
	id int not null auto_increment primary key,
	nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    posicion VARCHAR(50) NOT NULL,
    pais VARCHAR(50),
    fecha_nacimiento DATE,
    dorsal int UNIQUE,
    altura decimal (5,2) not null,
    peso decimal (4,2) not null
);
CREATE TABLE estadisticas_futbolistas (
    id INT not null AUTO_INCREMENT PRIMARY KEY,
    futbolista_id INT,
    partidos_jugados INT,
    goles INT,
    goles_encajados INT,
    asistencias INT,
    tarjetas_amarillas INT,
    tarjetas_rojas INT,
    FOREIGN KEY (futbolista_id) REFERENCES futbolistas(id)
);
CREATE TABLE staff (
    id INT not null AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    nacionalidad VARCHAR(50),
    cargo VARCHAR(50)
);
show tables;

insert into futbolistas values 
(null, 'Marc-André', 'ter Stegen', 'Portero', 'Alemania', '1992-04-30', 1, 187.00, 85.00),
(null, 'Iñaki', 'Peña', 'Portero', 'España', '1999-03-02', 13, 184.00, 78.00),
(null, 'João', 'Cancelo', 'Defensa', 'Portugal', '1994-05-27', 2, 182.00, 74.00),
(null, 'Alejandro', 'Balde', 'Defensa', 'España', '2003-10-17', 3, 175.00, 69.00),
(null, 'Ronald', 'Araujo', 'Defensa', 'Uruguay', '1999-03-06', 4, 188.00, 79.00),
(null, 'Iñigo', 'Martinez', 'Defensa', 'España', '1991-05-16', 5, 182.00, 76.00),
(null, 'Andreas', 'Christensen', 'Defensa', 'Dinamarca', '1996-04-09', 15, 187.00, 82.00),
(null, 'Marcos', 'Alonso', 'Defensa', 'España', '1990-12-27', 17, 188.00, 84.00),
(null, 'Sergi', 'Roberto', 'Defensa', 'España', '1992-02-06', 20, 178.00, 68.00),
(null, 'Joules', 'Kounde', 'Defensa', 'Francia', '1998-11-11', 23, 180.00, 75.00),
(null, 'Pablo', 'Gavira', 'Centrocampista', 'España', '2004-08-04', 6, 173.00, 70.00),
(null, 'Pedro', 'Gonzalez', 'Centrocampista', 'España', '2002-11-24', 8, 174.00, 60.00),
(null, 'Oriol', 'Romeu', 'Centrocampista', 'España', '1991-09-23', 18, 183.00, 83.00),
(null, 'Frenkie', 'de Jong', 'Centrocampista', 'Paises Bajos', '1997-05-11', 21, 181.00, 74.00),
(null, 'İlkay', 'Gündoğan', 'Centrocampista', 'Alemania', '1990-10-23', 22, 180.00, 80.00),
(null, 'Marc', 'Casadó', 'Centrocampista', 'España', '2003-09-23', 30, 172.00, 66.00),
(null, 'Fermín', 'López', 'Centrocampista', 'España', '2003-05-10', 32, 174.00, 67.00),
(null, 'Ferran', 'Torres', 'Delantero', 'España', '2000-02-28', 7, 184.00, 77.00),
(null, 'Robert', 'Lewandowski', 'Delantero', 'Polonia', '1988-08-20', 9, 185.00, 81.00),
(null, 'Raphael', 'Dias', 'Delantero', 'Brasil', '1996-12-13', 11, 176.00, 68.00),
(null, 'João', 'Félix', 'Delantero', 'Portugal', '1999-11-09', 14, 181.00, 70.00),
(null, 'Lamine', 'Yamal', 'Delantero', 'España', '2007-07-12', 27, 180.00, 64.00);

select * from futbolistas;
