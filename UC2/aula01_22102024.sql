CREATE DATABASE senac_copacabana
-- create a table
CREATE TABLE alunos (
  matricula INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  genero TEXT NOT NULL
);
-- insert some values
INSERT INTO alunos VALUES (1, 'Ryan', 'M');
INSERT INTO alunos VALUES (2, 'Joanna', 'F');
INSERT INTO alunos VALUES (3, 'Julia', 'F');
INSERT INTO alunos VALUES (4, 'Carlos', 'M');
-- fetch some values
SELECT * FROM alunos WHERE genero = 'F' AND matricula >= 2;

