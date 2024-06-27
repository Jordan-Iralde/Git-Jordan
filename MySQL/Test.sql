CREATE DATABASE IF NOT EXISTS PrueBaseDeDatos;
USE PrueBaseDeDatos;
CREATE TABLE Estudiantes (
ID INT AUTO_INCREMENT PRIMARY KEY,
Nombre VARCHAR(20) NOT NULL,
Apellido VARCHAR(20) NOT NULL
);

CREATE TABLE Materias (
ID_MATERIA INT AUTO_INCREMENT PRIMARY KEY,
NombreMateria VARCHAR(40) NOT NULL,
NOTA INT NOT NULL,
FOREIGN KEY (ID_Materia) REFERENCES Estudiantes(ID)
);

INSERT INTO Estudiantes(Nombre, Apellido) VALUES ('JORDAN', 'IRALDE');
INSERT INTO Materias(NombreMateria, Nota) VALUES ('Estructura y almacenamiento de datos', 9);

DROP TABLE Materias;

UPDATE Materias SET NOTA = 10 WHERE Id_Materia = 1;

SELECT * FROM Estudiantes;
SELECT * FROM Materias;