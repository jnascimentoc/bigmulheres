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

CREATE TABLE professores (
    id_professor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    genero TEXT NOT NULL
);

INSERT INTO professores VALUES (1,'Ana Maria', 'F');
INSERT INTO professores VALUES (2,'Carlos Henrique', 'M');
INSERT INTO professores VALUES (3,'Julia do Nascimento', 'F');
INSERT INTO professores VALUES (4,'Fernanda Moraes', 'F');
INSERT INTO professores VALUES (5,'Carlos Alberto', 'M');
INSERT INTO professores VALUES (6,'Viviane Almeida', 'F');
INSERT INTO professores VALUES (7,'Clarissa Castro', 'F');
INSERT INTO professores VALUES (8,'Fabio Paulo', 'M');

SELECT * FROM professores WHERE genero = 'M';

CREATE TABLE turma (
	id_turma INTEGER PRIMARY KEY,
    carga_horaria INTEGER NOT NULL,
    unidade_curricular TEXT NOT NULL,
    data_inicio DATE,
    data_final DATE,
    id_professor INTEGER
);



