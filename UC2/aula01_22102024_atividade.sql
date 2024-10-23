-- ATIVIDADE 
--Crie uma nova tabela chamada 'professores', com a mesma quantidade de características de 'alunos', fazendo ao menos duas injeções de dados e uma consulta.

CREATE TABLE professores (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    genero VARCHAR(1) NOT NULL,   
);

INSERT INTO professores VALUES (1,'Ana Maria', 'F');
INSERT INTO professores VALUES (2,'Carlos Henrique', 'M');
INSERT INTO professores VALUES (3,'Julia do Nascimento', 'F');
INSERT INTO professores VALUES (4,'Fernanda Moraes', 'F');
INSERT INTO professores VALUES (5,'Carlos Alberto', 'M');
INSERT INTO professores VALUES (6,'Viviane Almeida', 'F');
INSERT INTO professores VALUES (7,'Clarissa Castro', 'F');
INSERT INTO professores VALUES (8,'Fabio Paulo', 'M');

SELECT * FROM professores WHERE genero = 'F'