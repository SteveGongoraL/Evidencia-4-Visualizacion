create table Clientes (
    Matricula varchar2(8) primary key,
    Nombre varchar2(15) not null,
    ApellidoP varchar2(20) not null,
    ApellidoM varchar2(20) not null,
    Edad INT not null,
    Calle varchar2(30) not null,
    Numero INT not null,
    Carrera varchar2(45) not null,
    Municipio varchar2(30) not null,
    Estado varchar2(20) not null,
    Beca varchar2(5) not null,
    Materias varchar2(90) not null
);