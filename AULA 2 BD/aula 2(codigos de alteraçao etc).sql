use biblioteca;

/*
===========================ALTERANDO COLUNA==================================
ALTER TABLE Endereço ADD COLUMN CEP VARCHAR(12) NOT NULL;
*/


/*
======================ADICONANDO UMA RESTRIÇAO PARA O EMAIL========================
ALTER TABLE Usuario ADD CONSTRAINT emailUnico UNIQUE (email);
ALTER TABLE Autor ADD CONSTRAINT cpfUnico UNIQUE(cpf);
/*

/*
======================EDITANDO REGISTRO NA TABELA DO AUTO===========================
UPDATE Autor
SET cpf = 635
WHERE AutorID = 4;

SELECT * FROM Autor;
*/

/*
==========================TRANSFORMANFO ENDEREÇO EM UMA NOVA TABELA======================
create table Endereço(
	endereçoID INT auto_increment primary key,
    rua varchar(150) not null,
    numero int,
    complemento varchar(150),
    bairro varchar(100),
    cidade varchar(100) not null,
    userID int,
    foreign key(userID) references Usuario(userID)
);
*/

/*
============================APAGANDO UMA COLUNA EXPECIFICA===========================
ALTER TABLE Usuario DROP COLUMN Endereco;

*/

/*
=============================ADICIONANDO DADOS EM ENDEREÇOS===========================

INSERT INTO Endereço ( Rua, Numero, Complemento, Bairro, Cidade, userID, CEP) VALUES
	('rua A', '123', 'apto 1', 'bairro 1', 'cidade 1', 1, '1234421-218'),
    ('rua B', '456', null, 'bairro 2', 'cidade 2', 2, '1234421-219'),
    ('rua C', '789', 'casa 2', 'bairro 3', 'cidade 3', 3, '1234421-212'),
    ('rua D', '101', 'casa 3', 'bairro 2', 'cidade 1', 4, '11111-222'),
	('rua E', '222', NULL, 'bairro 4', 'cidade 4', 5, '1234421-218');
    
*/

/*=========================FAZENDO PESQUISA NO BANCO DE DADOS===========================*/
#SELECT NOME, ANO FROM Livro WHERE autorID = 1;

#SELECT NOME, ANO FROM Livro WHERE ANO  = 1882;
/*
SELECT
	Livro.nome AS NomeLivro,
    Autor.nome AS NomeAutor,
    Livro.ano AS AnoPublicaçao,
    Autor.cpf AS CPF
FROM
	Livro
		INNER JOIN 
	Autor ON Livro.autorID = Autor.autorID
WHERE
	Livro.autorID = 1;
*/

SELECT
	Usuario.nome, Livro.nome, Emprestimo.DataEmprestimo, Emprestimo.DataDevolucao
FROM
	Emprestimo
		INNER JOIN 
	Emprestimo ON Livro.autorID = Autor.autorID
WHERE
	Livro.autorID = 1;
