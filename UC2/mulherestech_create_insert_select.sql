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

INSERT INTO turma VALUES (1,300, 'Informatica Fundamental', 22042024, 25062024, 1);
INSERT INTO turma VALUES (2,200, 'Excel Avançado', 01072024, 01082024, 2);
INSERT INTO turma VALUES (3,400, 'FullStack', 22042024, 25082024, 3);
INSERT INTO turma VALUES (4,300, 'Analise de Dados - PowerBI', 05092024, 05112024, 2);
INSERT INTO turma VALUES (5,200, 'Excel Avançado', 22072023, 25082023, 1);
INSERT INTO turma VALUES (6,300, 'Informatica Fundamental', 22042023, 25062023, 1);
INSERT INTO turma VALUES (7,300, 'Informatica Fundamental', 22042023, 25062023, 1);
INSERT INTO turma VALUES (8, 250, 'Python para Iniciantes', 01092024, 30102024, 2);
INSERT INTO turma VALUES (9, 350, 'Desenvolvimento Web', 15082024, 15092024, 7);
INSERT INTO turma VALUES (10, 450, 'Data Science com R', 01062024, 31072024, 8);
INSERT INTO turma VALUES (11, 300, 'Gestão de Projetos', 01052024, 31052024, 1);
INSERT INTO turma VALUES (12, 200, 'Marketing Digital', 01072024, 31072024, 2);
INSERT INTO turma VALUES (13, 350, 'Introdução à Inteligência Artificial', 01082024, 31082024, 8);
INSERT INTO turma VALUES (14, 400, 'SQL para Análise de Dados', 15052024, 15062024, 7);
INSERT INTO turma VALUES (15, 500, 'Cibersegurança Básica', 01092024, 31102024, 5);



CREATE TABLE unidade (
	id_unidade INTEGER PRIMARY KEY,
    endereco TEXT NOT NULL,
    telefone FLOAT NOT NULL,
    email TEXT NOT NULL
    
);

INSERT INTO unidade VALUES (1, 'Rua A, 123', 11987654321, 'contato@unidade1.com');
INSERT INTO unidade VALUES (2, 'Avenida B, 456', 11876543210, 'contato@unidade2.com');
INSERT INTO unidade VALUES (3, 'Praça C, 789', 11765432109, 'contato@unidade3.com');
INSERT INTO unidade VALUES (4, 'Rua D, 101', 11654321098, 'contato@unidade4.com');
INSERT INTO unidade VALUES (5, 'Avenida E, 202', 11543210987, 'contato@unidade5.com');
INSERT INTO unidade VALUES (6, 'Rua F, 303', 11432109876, 'contato@unidade6.com');
INSERT INTO unidade VALUES (7, 'Praça G, 404', 11321098765, 'contato@unidade7.com');
INSERT INTO unidade VALUES (8, 'Rua H, 505', 11210987654, 'contato@unidade8.com');
INSERT INTO unidade VALUES (9, 'Avenida I, 606', 11109876543, 'contato@unidade9.com');
INSERT INTO unidade VALUES (10, 'Rua J, 707', 11098765432, 'contato@unidade10.com');
INSERT INTO unidade VALUES (11, 'Praça K, 808', 10987654321, 'contato@unidade11.com');
INSERT INTO unidade VALUES (12, 'Avenida L, 909', 10876543210, 'contato@unidade12.com');
INSERT INTO unidade VALUES (13, 'Rua M, 111', 10765432109, 'contato@unidade13.com');
INSERT INTO unidade VALUES (14, 'Praça N, 222', 10654321098, 'contato@unidade14.com');
INSERT INTO unidade VALUES (15, 'Rua O, 333', 10543210987, 'contato@unidade15.com');
