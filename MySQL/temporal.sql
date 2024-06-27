
/*		Esto es un comentario de multi-lineas
	-- Esto es un comentario de una linea
		NO IMPORTAN LAS MAYUSCULAS AL MOMENTO DE HACER UNA BASE DE DATOS o UNA TABLA
*/

-- CREATE DATABASE MiBD;
SHOW DATABASES;
USE mibd;		
-- Usa midb como schema, no se						

/*			CREATE TABLE
CREATE TABLE usu(
	id INT AUTO_INCREMENT PRIMARY KEY, 	Esta es la llave primaria, la cual va a ser la importante
    usuario VARCHAR(255)NOT NULL,			Este campo no puede estar vacio(NOT NULL)
    contraseña VARCHAR(255)NOT NULL			Este campo no puede estar vacio			
);
*/

-- Delete para borrar un registro

--

-- Date = 2023-9-7

/*			INSERT
Cuando se inserta un valor, se va a revisar los tipos de datos en orden como la lista en otro caso NULL
Cuando se llama la tabla, se le puede asignar cuales valores van a ser seleccionados

INSERT INTO Usu (usuario, contraseña) VALUES ('Jordan', 'jordanjuega');
INSERT INTO Usu (usuario, contraseña) VALUES ('Jordyn', 'pepeortiva');
INSERT INTO Usu (usuario, contraseña) VALUES ('Jordon', 'pepe');
*/

/*			ALTER TABLE		PARA MODIFICAR UNA TABLA
ALTER TABLE Usu MODIFY COLUMN id INT AUTO_INCREMENT;
 	Esto va a cambiar una columna (id) para que sea autoincrementado
*/
	-- # Table	Create Table
CREATE TABLE usu (
  id int NOT NULL AUTO_INCREMENT,
  usuario varchar(255) NOT NULL,
  contraseña varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);
INSERT INTO usu (usuario, contraseña) VALUES ('Jordan', 'jordanjuega');
INSERT INTO usu (usuario, contraseña) VALUES ('MATE', 'pepeortiva');
INSERT INTO usu (usuario, contraseña) VALUES ('SEBA', 'pepe');
	-- Esta es la tarea, como insertar los datos en las posiciones

SHOW CREATE TABLE usu;
	-- Crea la visualizacion de la alter tabla usu, parece


SELECT * FROM usu;
	-- Sirve para ver los elementos de la tabla 'usu'

SELECT * FROM usu WHERE id = 3;
	-- Sirve para ver los elementos de la tabla 'usu', donde el id sea 3 exclusivamente

SELECT * FROM usu WHERE  usuario = 'MATE' AND contraseña = 'pepeortiva' OR usuario = 'SEBA';
	-- Sirve para ver los elementos de la tabla 'usu' donde el usuario 'MATE' Y (condicion) su contraseña sea 'pepeortiva'
    
	-- Tambien se puede usar un BETWEEN (entre) cierto punto hasta cierto punto como condicion, esto despues del WHERE
    
	-- Tambien se puede agregar un LIKE '%busqueda%' para buscar algo, los % sirven para que no importe como esta escrito antes o desp.
    
    -- Se puede usar ORDER BY (valor int) asc/desc.		Abreviaciones de ascendente o descendente, esto despues de nombrar la tabla
    
-- SELECT MAX/MIN(valor int) AS MAYOR/MENOR FROM usu;
		-- Selecciona el valor MAX(maximo) o MIN(minimo) entre valores numericos
	

SELECT * FROM usu limit 4;
	-- Es un limite para mostrar los registros

UPDATE usu SET contraseña = 'contraseña' WHERE id = 2;
	-- Actualiza los valores de un lugar y de un valor(contraseña)

DELETE FROM usu WHERE id= 3;
	-- Borra desde usu donde este el id 3, no se soluciona

-- DROP DATABASE database_name;			Para borrar una base de datos
-- DROP TABLE table_name;				Para borrar una tabla
